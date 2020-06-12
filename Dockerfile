FROM centos:7

# Update the System
RUN yum update -y
RUN yum install -y curl wget gcc openssl-devel bzip2-devel libffi-devel make

# Install Python 3.7.7
RUN mkdir dependencies
COPY ./dependencies/Python-3.7.7.tgz /dependencies
RUN cd /dependencies && tar xzf Python-3.7.7.tgz
RUN cd /dependencies/Python-3.7.7 && sh configure --enable-optimizations && make altinstall
RUN rm -f /dependencies/Python-3.7.7.tgz

# Install pip
RUN mkdir -p /dependencies/pip
RUN cd /dependencies/pip && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.7 get-pip.py
RUN pip --version

# Install pipenv
RUN pip install --user pipenv
ENV PYTHON_BIN_PATH="/root/.local/bin"
ENV PATH="$PATH:$PYTHON_BIN_PATH"
ENV LC_ALL=en_US
RUN echo $PYTHON_BIN_PATH
RUN echo $PATH
RUN pipenv --version
ENV PYTHONIOENCODING=utf-8

RUN mkdir /workdir
WORKDIR /workdir


