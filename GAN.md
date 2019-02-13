#GAN

## basic idea
* Initialize generator and discriminator (G and D)
* **In each traning iteration:**
    1. Step1: Fix generator G and update discriminator D
    如下图所示，固定生成器，更新判别器，训练的时候从database里随机一些真实数据，生成器则随机生成数据，来更新判别器，这样做是为了训练判别器
    ![](imgs/GAN1.png)
    2. step2: Fix discriminator D and update generator G
    如下图所示，固定判别器，更新生成器，训练的时候生成器生成数据，判别器打分然后更新生成器，这样做是为了训练生成器
    ![](imgs/GAN2.png)