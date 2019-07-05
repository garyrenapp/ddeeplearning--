# sequence to sequence 

## ��������
![](imgs/seq2seq.png)
### ���ʣ�a<0>��ʲô
### ���ʣ�decoder�Ľ�����������
�ڱ���׶η��ﵥ�ʰ���ʱ��ÿ��������������(x1,x2...xT)�����õ�һ�������
����������������y1,y1��Ϊ��������y2,.....,��ô������һֱѭ����ȥ��?Ӧ���и�END OF�ķ��Ű�


## beam search ��������
�������(y1,y2,y3....)��һϵ�еĸ���,��Ҫ�ҳ�����������ߵĵ����,������̰���㷨���������y1,����y1����y2,��������y2....
![](imgs/beam-search.png)
### �����㷨
1. ��һ����ʱ������ͨ��ģ�ͼ���õ� $ y^{<1>} $�ķֲ����ʣ�ѡ��ǰB����Ϊ��ѡ�������beam width =3 ������ͼ��ʾ��"in", "jane", "september"
![](imgs/beam-search1.png)
2. �ڶ�����ʱ�������Ѿ�ѡ�����in��jane��September��Ϊ��һ�����ʵ����������ѡ��beam search���ÿ����һ�����ʿ��ǵڶ������ʵĸ��ʣ�������Ե��ʡ�in�������ǽ� $ y^{<1>} $ ='in'��Ȼ����ι��  ��������2��������$ y^{<2>} $  ��Ϊ�ڶ������ʵĸ�����������ǵ�ѡ�񷽷�Ϊ��$ P(y^{<2>},"in"|x)=P(y^{<2>}|"in",x) P("in"|x) $,�����õ�10000����ѡ��ͬ��"jane","Septeber"Ҳ���Եõ�10000����ѡ�ܹ�30000����ѡ��ѡ�������ߵ�ǰ3��������õ��Ľ���ǣ�
* in september
* jane is
* jane visits
3. ��������ʱ��ͬ�����ǽ����ǽ�$ y^{<1>} ='in'�� y^{<2>} ='september'��$Ȼ����ι��$ x^{<3>} $��������$ y^{<3>} $��Ϊ���������ʵĸ������10000��ѡ����������Ҳһ������30000��ѡ��ѡǰ3������������....,ֱ����ֹ�ھ�β����
**notice:** ���beam width =1,���̰���㷨��һ����

### beam search �Ľ� length normalization 
��Seq2Seq�е�beam search�㷨�в���beam search�������õ�ʹ����������ģ�͸����������У�������������������
$$\arg\max_{y} P( y^{<1>},y^{<2>},y^{<3>},...y^{<T_y>}|x^{<1>},x^{<2>},...x^{<T_x>})  $$
���� $ P(y^{<1>},y^{<2>},y^{<3>},...y^{<T_y>}|x)=P(y^{<1>}|x)P(y^{<2>}|y^{<1>},x)...P(y^{<T_y>}|y^{<1>},...,y^{<T_y-1>},x)$

������ǵ���������ģ�Ϳ��Կ����������ʽ��
$\arg\max_{y}\prod_{t=1}^{T_y} P(y^{<t>}|x,y^{<1>},...,y^{<t-1>}) $

**���������������**
1. ��ֵ���
��ʽ���������ʵĳ˻�,��ÿһ�<1,�ܶ���<1������,���������ֵ����(numerical underflow),����취�Ǽ�һ��log��ɸ������
$$\arg\max_{y} \sum_{t=1}^{T_y}{\log P(y^{<t>}|x,y^{<1>},...,y^{<t-1>})}$$

2. �����ڸ��̵ķ���
������˴���Խ������ԽС����ʹ��log����Ϊlog(<1)�Ǹ������������Ҳ����ɽ��ԽС�����Ի�������ڸ��̵ķ��롣
Ϊ�˽��������⣬���Ƕ�Ŀ�꺯�����й�һ�����õ���һ���Ķ�����ȻĿ�꺯��������ʽ��:
$$\arg\max_{y} \frac{1}{T_y^{a}}\sum_{t=1}^{T_y}{\log P(y^{<t>}|x,y^{<1>},...,y^{<t-1>})} $$
T_y�Ǿ��ӳ��ȣ�����ͨ�����ø�����͵ķ��������� a=0.7 ����� a=1 �����൱����ȫ�ó�������һ������� a=0 �����൱����ȫû�й�һ����
a��һ��������Ҫ����ʵ���������

### beam search �еĿ��B���ѡ��
������B�ĵ�����ʵ���зǳ���Ҫ��һ��������¹���

BԽ��
* �ŵ��ǣ��ɿ��ǵ�ѡ��Խ�࣬���ҵ��ľ���Խ��
* ȱ���ǣ�������۸����ٶ�Խ�����ڴ�����Խ��
BԽС
* �ŵ��ǣ��������С���ٶȿ죬�ڴ�ռ��ԽС
* ȱ���ǣ��ɿ��ǵ�ѡ����٣����û��ô��
��Seq2Seq�е�beam search�㷨������ѡ�� B=3 ����ʵ�������ֵ�е�ƫС���ڲ�Ʒ�У��������Կ����������赽10������Ϊ100���ڲ�Ʒϵͳ��˵�е���ˣ���Ҳȡ���ڲ�ͬӦ�á�

���ǶԿ��ж��ԣ�������ѹե��ȫ�����ܣ������и���õĽ�����������ģ�Ҳ�����������������Ϊ1000����3000����Ҳ��ȡ�����ض���Ӧ�ú��ض�������

����ʵ�����Ӧ��ʱ�����Բ�ͬ�������ֵ����B�ܴ��ʱ��������߻�Խ��Խ�١����ںܶ�Ӧ����˵��������1��Ҳ����̰���㷨��������Ϊ3����10����ῴ��һ���ܴ�ĸ��ơ����ǵ������1000���ӵ�3000ʱ��Ч����û��ô�����ˡ� 

### ����������������
���������㷨��һ�ֽ��������㷨��Ҳ����Ϊ����ʽ�����㷨������������ܱ�֤���ǿ��������ľ��ӣ���Ϊ��ÿһ���н���¼��Beam widthΪ3����10����100�ֵĿ��ܵľ��ӡ�

���ԣ�������ǵļ��������㷨���ִ�����Ҫ��ô���أ��������ȷ���Ǽ��������㷨�����˴�����ģ�ͳ����˴����أ���ʱ���������㷨������������ʾ�������á�

**����** 
ͬ���Է�����ӵ�Ӣ�ķ���Ϊ���ӣ���������Է�����ӵķ������м�ľ��ӣ������ǵ�ģ������ķ���������ľ��ӡ�ͨ�����ǵ�ģ�ͣ����Ƿֱ�������෭��ĸ��� $P(y^{*}|x)$ �Լ�ģ�ͷ���ĸ��� $P(\hat y|x)$ ���Ƚ��������ʵĴ�С��ͨ���Ƚ����Ǿ���֪������ΪBeam Search �㷨�����⻹��RNNģ�͵����⡣
![](imgs/error-analysis-beam-search.png)

- ���ʣ�����Ľ������ô��ģ�Ӧ����decode��ʱ��y<1>=jane�ĸ��ʣ���jane�����y<2>���visits�ĸ��������ۼ�
- $P(y^{*}|x) > P(\hat y|x)$ ����������෭�����Ҫ��beam search�� **����Beam search �㷨������**
- $P(y^{*}|x) <= P(\hat y|x)$ �������beam search ������������ĺã�**����������RNNģ�ͳ�����**
  
�Ը������ӽ��м�⣬�õ�ÿ�����Ӷ�Ӧ�ĳ����������ô�������������������㷨�����ģ�ʹ���ı������Ϳ�������ԵضԶ���֮һ���иĽ��������ˡ�
![](imgs/error-analysis-beam-search2.png)

## BLEU Score
���ڻ�������ϵͳ��˵��һ�����Զ�������һ�����Եķ��볣���ж�����ȷ�Һ��ʵķ��룬�����޷�������ͼ��ʶ��һ���й̶�׼ȷ�ȴ𰸣�������Բ�ͬ�ķ���������������������һ������Ǹ��õģ���һ������ϵͳ�Ǹ�����Ч�ġ���������Bleu score ������������ϵͳ��׼ȷ�ԡ���Bleu, bilingual evaluation understudy��

**������������**��
������ķ��﷭������ӣ����������ֲ�ͬ�ķ��룬�������ַ��붼����ȷ�ҽϺõķ�������
Bleu score �����������ǹ۲�������ɵķ������е�ÿһ�����Ƿ����������һ���˹��������Ĳο�֮�С�
����ͼReference1��2���˹�����Ĳο�
![](imgs/bleu.png)
- Precision: �۲���������ÿһ�����Ƿ�����ڲο���,������ȱ�����MT(machine translation) Output�ķ����������ȫ������the,������ȴ��7/7 ���Ⱥܸ�
- Modified Precision���Ľ�����㷨����ÿ����������һ���÷����ޣ������ο������г��ֵ����Ĵ�������ͼ��
  the���ʵ�����Ϊ2����

### Bleu score on bigrams 
�뵥���ʵ��������ƣ������������������ڵĵ�����Ϊһ����Ԫ����������Bleu�÷��������õ���������Ķ�Ԫ����ĵ÷ֺ�����Ӧ�ĵ÷����ޣ������õ��Ľ��ľ�ȷ�ȡ�
����ͼ��MT output��The cat the cat on the mat
��Ԫ��Ϊ(The cat)(cat the)(the cat)(cat on)(on the)(the mat),precision = 4/6
![](imgs/bleu-score-on-bigrams.png)
���ڲ�ͬ��n-gram�����Ǽ�������ľ�ȷ�ȵ÷ֵĹ�ʽ���£�
$$
{P_1}{\rm{ = }}\frac{{\sum\limits_{unigram \in \widehat y} {Coun{t_{clip}}(unigram)} }}{{\sum\limits_{unigram \in \widehat y} {Count(unigram)} }}
$$
$$
{P_n}{\rm{ = }}\frac{{\sum\limits_{n - gram \in \widehat y} {Coun{t_{clip}}(n - gram)} }}{{\sum\limits_{n - gram \in \widehat y} {Count(n - gram)} }}
$$

**scoreϸ��**

�õ�ÿ��n-gram��Bleu score�� $P_{n} $����$ P_{1}��P_{2}��P_{3}��P_{4}$ ��
���Bleu scores��
$BP \exp(\dfrac{1}{4}\sum_{n=1}^{4}P_{n})\\$

���У�BP(brevity penalty)��̳ͷ�����Ϊһ���������ӣ�����̫�̵ķ������ķ���ϵͳ���гͷ���

$BP = \left\{ \begin{array}{l} 1, if{\kern 1pt} {\kern 1pt} MT\_length > reference\_length{\kern 1pt} {\kern 1pt} \\ \exp (1 - MT\_length/reference\_length), otherwise \end{array} \right. $

Bleu score ��Ϊ��������ϵͳ��һ�ֵ�һ����ָ�꣬����һ����Ȼ���Ƿǳ�����������ȴҲ�ǳ��õ�Ч������ӿ�������������������Ľ��̣��Ի���������и����Ե�Ӱ�졣ͬʱ��Bleu score�Դ�������ı����ɵ�ģ�;�����Ч�������ֶΡ�

## image captioning
**����:** encoder����׶���CNN��ͼ����б���

![](imgs/image-caption.png)

## Attention Model
**�����Ӵ��ڵ�����**

��������ǰ��ı���ͽ����RNNģ�ͣ������ܹ�ʵ�ֽ�Ϊ׼ȷ�Ȼ��������������ڶ̾�����˵����������ʮ�����õģ���������Ǻܳ��ľ��ӣ�����Ľ���ͻ��

����������������˹������ʱ������������Ҳ������������RNNģ��һ����������������ӣ��ٽ�����Ӧ���������Ϊ���������������Ǻ��ѵģ�����������һ����һ���ֵؽ��з��롣�������RNNģ�͵Ľṹ����Bleu score���ھ��ӳ��ȳ���һ��ֵ��ʱ��ͻ��½�����ͼ�е���ɫ����ʾ���������ע�������ƣ�������ķ�����̷ǳ����ƣ���Ҳ��һ����һ���ֵؽ��г����ӵķ��룬����õ��ķ�������Bleu��������ͼ����ɫ����ʾ��
![](imgs/attention-bleu.png)
attention���ƾ��Ƿ�������ÿ��$ y^{<t>}$ ʱ�����ض���context��Ϣ $c^{<t>} $������ԭ���в�ͬ�Ĳ��ֶ��ڷ��뵱ǰ�ʻ��в�ͬ��Ȩ�أ�Ч�����úܶ࣬��������Գ����ӵ�ʱ������ͼ3�е���ɫ������ʾ��

attentionģ������ͼ����ʾ����ģ�Ͱ�������ģ�飬����encoderģ�飬decoderģ�飬�м��attention���������ڷ���ÿ�� $y^{<t>}$ ʱ����������Ϣ $context^{<i>}$ ��Ҳ����$ c^{<t>} $.

<table>
<td> 
<img src="imgs/attn_model.png" style="width:500;height:500px;"> <br>
</td> 
<td> 
<img src="imgs/attn_mechanism.png" style="width:500;height:500px;"> <br>
</td> 
</table>

����encoder����Ϊbi-lstmģ�飬���ÿ������������ʾ $x^{<t>}$ ����ǰ�򴫲��õ�������Ϊ��
$a^{<t>}=[\overrightarrow{a}^{<t>},\overleftarrow{a}^{<t>}] $

decoder�������ÿ��$ y^{<t>} $���м���ʱ������3�������룺

1. ��������ϢҲ����ͼ�е�$ context^{<t>}$
2. �ϸ�ʱ�̵�LSTM cell������״̬ $s^{<t-1>}$ (�����Ҫ�����л����ű�ʾ��ͨ�����ز�״̬��$ h^{<t-1>} $����ʾ)
3. �ϸ�ʱ�̵�decoder���$ y^{<t-1>}$
��attentionģ�鲿�֣������� $\alpha^{<t,\tilde{t}>}$ ��ʾ�ڷ��� $y^{<t>}$ ʱӦ�û����� $a^{<\tilde{t}>} $�ϵ�ע��������������˼��������� $context^{<t>} $��ʽ���£�

$$context^{<t>}=\sum_{\tilde{t}=1}^{T_x}{\alpha^{<t,\tilde{t}>}a^{<\tilde{t}>}}$$
$$ {a^{ < t,t' > }} = \frac{{\exp ({e^{ < t,t' > }})}}{{\sum\limits_{t' = 1}^{{T_x}} {\exp ({e^{ < t,t' > }})} }} $$
${a^{ < t,t' > }}$�ļ���ϸ���� ��ϰ���one_step_attention ������
![](imgs/attention-att.png)

```python

def model(Tx, Ty, n_a, n_s, human_vocab_size, machine_vocab_size):
    """
    Arguments:
    Tx -- length of the input sequence
    Ty -- length of the output sequence
    n_a -- hidden state size of the Bi-LSTM
    n_s -- hidden state size of the post-attention LSTM
    human_vocab_size -- size of the python dictionary "human_vocab"
    machine_vocab_size -- size of the python dictionary "machine_vocab"

    Returns:
    model -- Keras model instance
    """
    
    # Define the inputs of your model with a shape (Tx,)
    # Define s0 and c0, initial hidden state for the decoder LSTM of shape (n_s,)
    X = Input(shape=(Tx, human_vocab_size))
    s0 = Input(shape=(n_s,), name='s0')
    c0 = Input(shape=(n_s,), name='c0')
    s = s0
    c = c0
    
    # Initialize empty list of outputs
    outputs = []
    
    ### START CODE HERE ###
    
    # Step 1: Define your pre-attention Bi-LSTM. Remember to use return_sequences=True. (�� 1 line)
    a = Bidirectional(LSTM(n_a,return_sequences=True),name='bidirectional_1')(X)
    
    # Step 2: Iterate for Ty steps
    for t in range(Ty):
    
        # Step 2.A: Perform one step of the attention mechanism to get back the context vector at step t (�� 1 line)
        context = one_step_attention(a,s)
        
        # Step 2.B: Apply the post-attention LSTM cell to the "context" vector.
        # Don't forget to pass: initial_state = [hidden state, cell state] (�� 1 line)
        s, _, c = post_activation_LSTM_cell(context,initial_state=[s,c])
        
        # Step 2.C: Apply Dense layer to the hidden state output of the post-attention LSTM (�� 1 line)
        out = output_layer(s)
        
        # Step 2.D: Append "out" to the "outputs" list (�� 1 line)
        outputs.append(out)
    
    # Step 3: Create model instance taking three inputs and returning the list of outputs. (�� 1 line)
    model = Model([X,s0,c0],outputs)
    
    ### END CODE HERE ###
    
    return model
```
## �����ּ��

һ�ֿ��Լ�Ӧ�õĴ����ּ���㷨������ʹ��RNNģ�ͣ�����Ƶ�źŽ�������ͼת���õ�ͼ����������ʹ����Ƶ���������뵽RNN����Ϊ���ǵ����롣������ı�ǩ�����ǿ����Դ�����ǰ����������Ϊ0�������ֺ���������Ϊ1��
![](imgs/trigger-word-detection.png)

### ��������
������Ƶ���ݺ��ѱ�ע�����positive��negative��background��ƵƬ�����ϳ�ѵ���������ںϳɵĹ����У����������ѡ��һ��10s��background��Ȼ������Ĳ���0-4��positive���������Ĳ���0-2��negative�� ����һ�����ǿ�����ȷ��֪�������ֵ�λ���ˣ����Եõ���ǩy

**�ڸ�дbackground��ͬʱ������ǩ**
���ѡ���background�ǲ��������֡�activate���ģ���˴�ʱ��y<t>=0��������positive���ʺ���Ҫ����Ӧ��ʱ�䲽���Ϊ1�����磬������5s�����롰activate��������Ϊ50��ʱ�䲽������ô��ʱy<688>=y<689>=...=y<737>=1,����ͼ��ʾ��
![](imgs/trigger-word-detection2.png)

###ģ�ͽṹ
![](imgs/model.png)



### teacher forcing
ѵ��


### ��������ʵ��
https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/eager/python/examples/nmt_with_attention/nmt_with_attention.ipynb


### attention��ʽ
https://stackoverflow.com/questions/44238154/what-is-the-difference-between-luong-attention-and-bahdanau-attention
https://blog.csdn.net/BVL10101111/article/details/78470716

Luong Attention
Bahdanau Attention


### attention�Ŀ��ӻ�
