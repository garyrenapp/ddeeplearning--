http://landcareweb.com/questions/21841/timedistributedceng-zai-keraszhong-de-zuo-yong-shi-shi-yao

在 keras  - 在构建顺序模型时 - 通常是第二维（一个在样本维度之后） - 与a相关 time 尺寸。这意味着，例如，如果您的数据是 5-dim 同 (sample, time, width, length, channel) 你可以使用卷积层 TimeDistributed （适用于 4-dim 同 (sample, width, length, channel)）沿着时间维度（将相同的层应用于每个时间片）以获得 5-d 输出。

这个案子 Dense 是那个 keras 从2.0版开始 Dense 默认情况下仅应用于最后一个维度（例如，如果您申请 Dense(10) 输入形状 (n, m, o, p) 你会得到形状的输出 (n, m, o, 10)）所以在你的情况下 Dense 和 TimeDistributed(Dense) 是等价的。