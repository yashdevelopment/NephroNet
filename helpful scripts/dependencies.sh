# AUTHOR: YASH S
# Installs python dependencies and initiates accelerate environment

cd diffusers
pip install -e .
cd ../
pip install -r diffusers/examples/dreambooth/requirements.txt
accelerate config default
echo "Dependencies installed and accelerate environment has been initiated."
