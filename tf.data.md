```python

class Dataset():
    def __init__(self):
        self.bucket_map = {} 
    
    def _pad_img(self,imgs):       
        _max_w , _max_h = 0,0
        for img in imgs:
            h,w = img.shape[0:2]
            _max_w = max(_max_w,w)
            _max_h = max(_max_h,h)
            
        _pad_imgs = np.zeros((len(imgs),_max_h,_max_w),dtype='float32')
        for idx,img in enumerate(imgs):
            _pad_imgs[idx,:img.shape[0],:img.shape[1]] = img
        _pad_imgs = np.expand_dims(_pad_imgs,-1)
        return _pad_imgs
        
    def _preprocess_image(self,image_file_paths,vectors):
        imgs = [] 
        for idx,i_p in enumerate(image_file_paths):
            _i_p = bytes.decode(i_p.numpy())
            img = cv2.imread(_i_p,cv2.IMREAD_GRAYSCALE)
            img = img / 255.0 - 0.5
            imgs.append(img)
            
        _pad_imgs = self._pad_img(imgs) 
        
        return _pad_imgs,vectors

    def _preprocess_image2(self,image_file_paths,vectors):
        _pad_imgs,vectors = self._preprocess_image(image_file_paths,vectors)
        return _pad_imgs,vectors,image_file_paths
    
    def _bucket_map(self,image_shape):
        '''按照图片的shape进行bucket，对不同的shape进行编号
        '''
        _image_shape = tuple(image_shape.numpy())
        if(_image_shape not in self.bucket_map):
            self.bucket_map[_image_shape] = len(self.bucket_map) + 1
            
        return tf.cast(self.bucket_map[_image_shape],dtype=tf.int64)

    def _compose(self,imgs,vectors):
        imgs.set_shape([None,None,None,1])
        vectors.set_shape([None,None])
        return ((imgs,vectors),vectors)

    def create(self,formulas_data,buffer_size = 1000,batch_size = 8,batch_size_window = 80 ,mode='train'):
        if(mode not in ('train','val','test')):
            raise ValueError('mode {} not  be supported'.format(mode))

        dataset = tf.data.Dataset.from_tensor_slices(formulas_data)

        if(mode=='train'):
            dataset = dataset.shuffle(buffer_size = buffer_size)
            dataset = dataset.repeat()   
            
        dataset = dataset.apply(
            tf.data.experimental.group_by_window(
                # Use feature as key
                key_func=lambda elem: tf.py_function(
                    self._bucket_map,[elem['image_shape']],tf.int64),
                # Convert each window to a batch
                reduce_func=lambda _, window: window.batch(batch_size),
                # Use batch size as window size
                window_size=batch_size ))

        if(mode =='train' or mode =='val'):
            dataset = dataset.map(
                lambda elem : tf.py_function(
                    self._preprocess_image,[elem['path'],elem['formalus_vector']],[tf.float32,tf.int32]
                ),num_parallel_calls = tf.data.experimental.AUTOTUNE)#
            dataset = dataset.map(lambda x,y: self._compose(x,y),num_parallel_calls = tf.data.experimental.AUTOTUNE)
        elif(mode == 'test'):
            dataset = dataset.map(
                lambda elem : tf.py_function(
                    self._preprocess_image2,[elem['path'],elem['formalus_vector']],[tf.float32,tf.int32,tf.string]
                ),num_parallel_calls = tf.data.experimental.AUTOTUNE)#

        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        return dataset 
    
    

```