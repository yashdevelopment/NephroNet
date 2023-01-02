![NEPHRONET_BANNER-removebg](https://user-images.githubusercontent.com/69687926/210128807-13c16e13-4502-43ea-9654-f94a16fdf03b.png)
## NephroNet: A Novel Program for Identifying Renal Cell Carcinoma and Generating Synthetic Training Images with Convolutional Neural Networks and Diffusion Models   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7498108.svg)](https://doi.org/10.5281/zenodo.7498108)

### Updates
Currently in development. Progress:

Part 1: Classifying
- [x] Split trainng, validation, and testing samples
- [x] Generate 20,000 patches per directory (Data Processing)
- [x] Model Training (ResNet-18 @ 40 Epochs)
- [x] Testing on Whole-Slide Images
- [x] Implement thresholding with a grid search
- [x] Visualization of predictions
- [x] Final Testing & Confusion Matrix

Part 2: Generating
- [x] Data Preprocessing
- [x] Stable Diffusion ([online](https://diffusion.chat), no modifiers)
- [x] Dreambooth Text-to-Image (CompVis trained on DHMC dataset, fine-tuned UNet and later fine-tuned text encoder)
- [x] Textual Inversion (will try on several tokens such as types of RCC)
- [ ] Text-to-Image (if time + money allows)
- [ ] Unconditional Image Generation (if time + money allows)

More to come soon (including results, research paper, code, etc).
