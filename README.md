# Image to ASCII Text Art APP
### The project consists of an image to ASCII text converter.

# Requirements
- Python >= 3.9
- Docker (Optional)

# Run project
## For python you must create a virtual environment.

```bash
virtualenv myenv
```
### Windows
```
myenv\Scripts\activate
```
### MacOS & Linux
```bash
source myenv/bin/activate
```
### Install requeriments
```bash
pip install -r requirements.txt
```

## For docker

### Create image
```bash
sudo docker build -t ascii .
```
### Exec container
```bash
sudo docker run -it -v "/home/user/img_to_ascii/:/workspace/" ascii bash
```

## Run app
```bash
python main.py
```

# Examples
![IMAGE EXAMPLE](https://github.com/x4leqxinn/image-to-ascii-script/blob/main/app/examples/IMG_VERSION.png)
![ASCII RESULT](https://github.com/x4leqxinn/image-to-ascii-script/blob/main/app/examples/ASCII_VERSION.png)



