# Fission_Analysis_VAMOS
Fission Analysis Vamos --> FAV --> Is the repository for VAMOS spectrometer analysis code applied to fission

## Installation<br/>
Use git clone in terminal:
```bash
git clone https://github.com/ferdani/Fission_Analysis_VAMOS.git  <FolderNameYouWant>
```
Enter inside the folder:
```bash
cd <FolderNameYouWant>
```
Use a virtual environment to install inside it all packages in an easy way:
```bash
sudo pip install virtualenv
```
```bash
virtualenv -p python3 <VirtualEnvNameYouWant>
```
Now, a virtual environment with this name <VirtualEnvNameYouWant> is created. Enter inside the virtual environment
```bash
source <PathToVirtualEnv>/<VirtualEnvNameYouWant>/bin/activate
```
And install all packages directly inside (only inside because is a Virtual Environment):
```bash
pip install -r requirements.txt
```

## How to use<br/>
Use with python 3.7.3 , with ROOT 6.17/01 and with root_numpy. Open a new terminal inside the Code-Folder:
Load ROOT:
```bash
source <Path_to_folder>/bin/thisroot.sh
```
Load Virtual Enviroment (is useful to create an alias):
```bash
source <PathToVirtualEnv>/<VirtualEnvNameYouWant>/bin/activate
```
Now, run an independent module
```bash
source run_module.sh
```
with the correct selection module inside the run_module.sh
