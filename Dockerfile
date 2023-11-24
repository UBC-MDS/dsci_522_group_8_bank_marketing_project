FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y pandas=2.1.3 \ 
    scikit-learn=1.3.2 \ 
    ipykernel=6.26.0 \
    altair=5.1.2 \ 
    pip=23.3.1 \
    ipykernel=6.26.0 \
    scipy=1.11.3 \ 
    numpy=1.26.0