



```python
    def _positional_encoding_2d(self,d_model,max_h = 100,max_w = 300):
        '''位置编码

            预先计算二维位置编码,这里设定了一个很大的max_h max_w,这样无需每次重复计算，
            每次索引取所需要的维度即可
            notice : tensor object does not support item assignment,这里用numpy 替代

            args:
             d_model : 特征维度
             max_h : 高度
             max_w : 宽度

            returns :
             二维tensor
        '''
        if(d_model % 4 !=0):
            raise ValueError('d_model % 4 !=0 ')
        pe = np.zeros((max_h,max_w,d_model))
      #print('pe shape:',pe.shape)
        d_half_model = d_model // 2 

        div_term = 1 / np.power(
                                  10000,
                                  np.arange(0,d_half_model,2) / d_half_model
                                  )
      
        pos_w = np.arange(max_w)[:,np.newaxis]
        #print('pos_w * div_term shape :',(pos_w * div_term).shape)
        pe[:,:,0:d_half_model:2] = np.sin(pos_w * div_term)
        pe[:,:,1:d_half_model:2] = np.cos(pos_w * div_term)
        pos_h = np.arange(max_h)[:,np.newaxis,np.newaxis]
        #print('pos_h * div_term shape :',(pos_h * div_term).shape)
        pe[:,:,d_half_model::2] = np.sin(pos_h * div_term)
        pe[:,:,d_half_model+1::2] = np.cos(pos_h * div_term)

        return tf.cast(pe,dtype=tf.float32)
 
```

```python
from .backend import keras
from .backend import backend as K


class TrigPosEmbedding(keras.layers.Layer):
    """Position embedding use sine and cosine functions.

    See: https://arxiv.org/pdf/1706.03762

    Expand mode:
        # Input shape
            2D tensor with shape: `(batch_size, sequence_length)`.

        # Output shape
            3D tensor with shape: `(batch_size, sequence_length, output_dim)`.

    Add mode:
        # Input shape
            3D tensor with shape: `(batch_size, sequence_length, feature_dim)`.

        # Output shape
            3D tensor with shape: `(batch_size, sequence_length, feature_dim)`.

    Concat mode:
        # Input shape
            3D tensor with shape: `(batch_size, sequence_length, feature_dim)`.

        # Output shape
            3D tensor with shape: `(batch_size, sequence_length, feature_dim + output_dim)`.
    """
    MODE_EXPAND = 'expand'
    MODE_ADD = 'add'
    MODE_CONCAT = 'concat'

    def __init__(self,
                 mode=MODE_ADD,
                 output_dim=None,
                 **kwargs):
        """
        :param output_dim: The embedding dimension.
        :param kwargs:
        """
        if mode in [self.MODE_EXPAND, self.MODE_CONCAT]:
            if output_dim is None:
                raise NotImplementedError('`output_dim` is required in `%s` mode' % mode)
            if output_dim % 2 != 0:
                raise NotImplementedError('It does not make sense to use an odd output dimension: %d' % output_dim)
        self.mode = mode
        self.output_dim = output_dim
        self.supports_masking = True
        super(TrigPosEmbedding, self).__init__(**kwargs)

    def get_config(self):
        config = {
            'mode': self.mode,
            'output_dim': self.output_dim,
        }
        base_config = super(TrigPosEmbedding, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def compute_mask(self, inputs, mask=None):
        return mask

    def compute_output_shape(self, input_shape):
        if self.mode == self.MODE_EXPAND:
            return input_shape + (self.output_dim,)
        if self.mode == self.MODE_CONCAT:
            return input_shape[:-1] + (input_shape[-1] + self.output_dim,)
        return input_shape

    def call(self, inputs, mask=None):
        input_shape = K.shape(inputs) ## 假设shape = [11,27,256]
        if self.mode == self.MODE_ADD:
            batch_size, seq_len, output_dim = input_shape[0], input_shape[1], input_shape[2]
            ## pos_input shape = [11, 27]
            #[[0,1,2,3,.....26],
            # [0,1,2,3,.....26],
            # .............]
            pos_input = K.tile(K.expand_dims(K.arange(0, seq_len), axis=0), [batch_size, 1])
        elif self.mode == self.MODE_CONCAT:
            batch_size, seq_len, output_dim = input_shape[0], input_shape[1], self.output_dim
            pos_input = K.tile(K.expand_dims(K.arange(0, seq_len), axis=0), [batch_size, 1])
        else:
            output_dim = self.output_dim
            pos_input = inputsx
        if K.dtype(pos_input) != K.floatx():
            pos_input = K.cast(pos_input, K.floatx())
        ##evens shape = [128]  内容是[0,2,4,.....254]
        evens = K.arange(0, output_dim // 2) * 2  
        ##odds shape = [128] 内容是[1,3,5,....,255]
        odds = K.arange(0, output_dim // 2) * 2 + 1
        ##even_embd shape = [11, 27, 128]
        #array([0.       , 0.0078125, 0.015625 , 0.0234375, 0.03125  , 0.0390625,
        #0.046875 , 0.0546875, 0.0625   , 0.0703125, 0.078125 , 0.0859375,......
        even_embd = K.sin(
            K.dot(
                K.expand_dims(pos_input, -1),
                K.expand_dims(1.0 / K.pow(
                    10000.0,
                    K.cast(evens, K.floatx()) / K.cast(output_dim, K.floatx())
                ), 0)
            )
        )
        ###odd_embd shape = [11, 27, 128]
        odd_embd = K.cos(
            K.dot(
                K.expand_dims(pos_input, -1),
                K.expand_dims(1.0 / K.pow(
                    10000.0, K.cast((odds - 1), K.floatx()) / K.cast(output_dim, K.floatx())
                ), 0)
            )
        )
        ###embd shape = [11, 27, 128,2]
        embd = K.stack([even_embd, odd_embd], axis=-1)
        #output shape = [11, 27, 256]
        output = K.reshape(embd, [-1, K.shape(inputs)[1], output_dim])
        if self.mode == self.MODE_CONCAT:
            output = K.concatenate([inputs, output], axis=-1)
        if self.mode == self.MODE_ADD:
            output += inputs
        return output
```
