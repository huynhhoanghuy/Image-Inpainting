# Image-Inpainting
Medical Image Inpainting by GANs method
# GatedConvolution-TF
An unofficial TensorFlow implementation of Free-Form Image Inpainting with Gated Convolution (https://arxiv.org/abs/1806.03589).

#### This is still an ongoing implementation ####

### Dependencies
1. Python 3
2. Tensorflow >= 1.4
3. Neuralgym (https://github.com/JiahuiYu/neuralgym)

### To do list
- [x] Create filelist.
- [x] Modify inpaint.yml to set DATA_FLIST, LOG_DIR, IMG_SHAPES and other parameters.
- [ ] Slim model by 25% -  Still training with original width of the model. You can slim the model by 25% by setting cnum = 32 * 0.75.
- [ ] Provide pretrained model - Will provide after finishing training.
- [ ] Provide loss graph - Will update soon.
- [ ] Provide test results - Still training.

### Code References
1. https://github.com/JiahuiYu/generative_inpainting
