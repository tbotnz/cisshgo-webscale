# cisshgo-webscale
simple CFN template generator for large scale cisshgo deployments

### pre-reqs
- security group in aws allowing inbound TCP ports 10000, 11000

### using

update the boilerplate with your security group name

```
        SecurityGroups:
        - launch-wizard-11
```

adjust the number of instances needed in the template generator

```# adjust the number of CFN instances needed
for x in range(0, 100):
    manip_str = f"""  csgo{x}:
 ```
 
 run the template generator
 
 ```python3 generate_template.py```

upload the template to CFN and have fun
