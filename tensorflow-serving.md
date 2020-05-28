
## docker 部署
```
docker run --gpus '"device=1"' -p 8501:8501 --mount type=bind,source=/data/mahuichao/math_equation_fit_input_feed/tmp/signature/,target=/models/math -e MODEL_NAME=math -t tensorflow/serving:latest-gpu &
```

```
data = json.dumps({'instances':x[0:1].numpy().tolist(),'signature_name':'predict_beamsearch4'})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/math:predict',data=data, headers=headers)
predictions = numpy.array(json.loads(json_response.text)["predictions"])
predictions[0]['output_0']
```


## saved model
```python
eval_batch_decoder = seq2seq.eval_batch_decoder.get_concrete_function(tf.TensorSpec([None,None,None,1],tf.float32))
tf.saved_model.save(seq2seq,'./tmp/signature/1',signatures= {"predict_beamsearch4":eval_batch_decoder})
im = tf.saved_model.load('./tmp/signature/1')
#接口调用
infer = im.signatures['predict_beamsearch4']
#类方法调用
im.eval_batch_decoder(x[0:1])
```