import shutil
import os

def clean_directory(target_path):
  if os.path.exists(target_path) is False:
    raise Exception("The `public` directory does not exist.")
  if len(os.listdir(target_path)) > 0:
    shutil.rmtree(target_path)
    os.mkdir(target_path)

# copy contents from a src path to a target path
def file_copier(src, dst):
  if os.path.exists(src) is False:
     raise Exception("The specified directory does not exist.")
  clean_directory(dst)

  src_contents = os.listdir(src)
  for item in src_contents:
    cur_path = os.path.join(src, item)
    new_path = os.path.join(dst, item)
    if os.path.isfile(cur_path):
      shutil.copy(cur_path, dst)
    else:
      os.mkdir(new_path)
      file_copier(cur_path, new_path)

