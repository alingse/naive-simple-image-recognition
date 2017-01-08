# 简单验证码基本识别训练流程

## base

4 steps to train

 - download.py
 - binary.py
 - split.py
 - rename.py

### steps 

1. download

 code your `down_image.py:get_img` 
 
 `python download.py --count 100`

2. binary
  
  code your `bin_image.py:bin_img`
  
  `python binary.py`
  
3. split
   
   code your `split_image.py:split_kwargs` or more `split_image.py:split_mat`
   
4. rename

   `python rename.py --help`

   `--chars`

   `--without`

   `--upper`

5. test

### test

`python download.py test test.jpg`

`python binary.py test test.jpg`

`python split.py test test.jpg.bmp`

`python test.py test.jpg`

### release

`./mkrelease.sh`


### usage
	
  ```python
  from verify.py import read_img
  from verify.py import read_content
    
  result = read_img(img)  
  [('6', 1.0), ('6', 1.0), ('4', 0.66796875), ('6', 1.0)]
  ```
