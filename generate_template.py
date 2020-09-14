
# adjust the number of CFN instances needed
for x in range(0, 100):
    manip_str = f"""
    csgo{x}:
      Type: AWS::EC2::Instance
      Properties:
        InstanceType: t2.large
        ImageId: ami-0f87b0a4eff45d9ce
        SecurityGroups:
        - launch-wizard-11
        KeyName:
         Ref: KeyName
        UserData:
          Fn::Base64: 
            "Fn::Join" : [
              "",
              [
                "#!/bin/bash\\n",
                "apt -y remove 'golang-*'\\n",
                "cd /home/ubuntu && wget https://dl.google.com/go/go1.13.9.linux-amd64.tar.gz\\n",
                "git clone https://github.com/tbotnz/cisgo-ios\\n",
                "tar xf go1.13.9.linux-amd64.tar.gz\\n",
                "mv go /usr/local/go-1.13\\n",
                "cd /etc/systemd/system\\n",
                "echo \\"[Unit]\\" > cisgo.service\\n",
                "echo \\"Description=herp\\" >> cisgo.service\\n",
                "echo \\"After=network.target\\" >> cisgo.service\\n",
                "echo \\"\\" >> cisgo.service\\n",
                "echo \\"[Service]\\" >> cisgo.service\\n",
                "echo \\"User=root\\" >> cisgo.service\\n",
                "echo \\"WorkingDirectory=/home/ubuntu/cisgo-ios/\\" >> cisgo.service\\n",
                "echo \\"ExecStart=/usr/local/go-1.13/bin/go run cis.go -listners 1000\\" >> cisgo.service\\n",
                "echo \\"Restart=always\\" >> cisgo.service\\n",
                "echo \\"\\" >> cisgo.service\\n",
                "echo \\"[Install]\\" >> cisgo.service\\n",
                "echo \\"WantedBy=multi-user.target\\" >> cisgo.service\\n",
                "echo \\"\\" >> cisgo.service\\n",
                "systemctl daemon-reload\\n",
                "sleep 10\\n",
                "systemctl enable cisgo\\n",
                "systemctl start cisgo\\n",
                "reboot\\n",
                "\\n"
              ]
            ]
        Tags:
          - Key: Name
            Value: cisgo instance{x}
          - Key: Type
            Value: Worker Instance{x}"""
    with open("boilerplate.yml", "a") as myfile:
        myfile.write(manip_str)
