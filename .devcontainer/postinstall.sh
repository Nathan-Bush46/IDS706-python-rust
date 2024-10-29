# These commands are run after the docker image is built.
pip install -r requirements.txt
#python -m nltk.downloader punkt
# get rust installed (quick but works)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
