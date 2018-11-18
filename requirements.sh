pip3 install -r requirements.txt
sudo apt install python-opengl xvfb libxrender1 libxtst6 libxi6 
sudo Xvfb :1 -screen 0 1024x768x24 </dev/null & export DISPLAY=":1"