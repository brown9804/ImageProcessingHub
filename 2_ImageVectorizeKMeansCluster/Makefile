create-env:
	@echo "Creating Python virtual environment..."
	python -m venv env

install: create-env
	@echo "Activating Python virtual environment..."
	. env/bin/activate
	@echo "Installing Python packages..."
	pip install scikit-image
	pip install numpy
	pip install matplotlib
	pip install pillow
	pip install opencv-python
	pip install svgwrite
	@echo "Installation completed."

.PHONY: create-env install
