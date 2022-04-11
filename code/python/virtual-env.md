
# Conda
## Create env
```
conda create -n env1 python=3.10
conda activate env1
conda deactivate
```

## Install a package
```
conda install pandas
conda install pandas=1.4.1
```

## Update environment using environment.yml
Create `environment.yml` file
```
cat << EOF > environment.yml
name: env1

dependencies:
  - pandas=1.4.1
EOF
```

Update environment
```
conda env update --file environment.yml  --prune
```

## Clone env
```
conda create --name env2 --clone env1
```

# venv
```
python -m venv venv2
source venv2/bin/activate
deactivate
```