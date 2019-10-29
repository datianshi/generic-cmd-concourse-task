## Why

**Abstract things as you need and keep refactoring!~**
**Reduce duplicate code**

Concourse is used at Pivotal to leverage docker containers to orchestrate PAAS installation/deployment.

Assume we have a need to install an on premises kubernetes environment:

We need to integrate with following systems:

* switches
* iDrac
* re-image system
* Software Defined Networking
* Virtualization environment vSphere
* .....

In order to automate the configuration across multiple environments and multiple systems.

People usually create a shell script to do ssh/api interaction with the system, and then create a concourse task to run the script inside the container. The number of scripts/concourse tasks grows fast and It is hard to maintain and iterate, while I would like to separate the concerns.

## How

* Each system has its own implementation of command line tool to take care of the system level interaction. The command line can be used by **either** orchestrators or operators.

* Concourse behave as a generic invoker/batch orchestrate systems' configuration

* There are couple of opportunities to extract the generic part:
  * Most system has authentication with username, password, host/ip and port
  * Concourse execute commands multiple time in a loop to support batch configuration
  * Concourse pass environment variable and arguments to the system's command line

## Example

* Command - test.sh
  A script to print out username password host and arguments  
* Sample configuration
  ```
  config:
    credentials:
    - username: admin1
      password: admin1
      host: abc.com
    - username: admin2
      password: admin2
      host: bcd.com
    - username: admin3
      password: admin3
      host: ghf.com
    command:
      exec: ./pipeline/test.sh
      argument:
      - --what hello
      - --word shaozhen
  ```

* Run
  ```fly -t concourse execute -c task.yml -i pipeline=.```

  ```
  admin1 admin1 abc.com --what hello --word shaozhen
  admin2 admin2 bcd.com --what hello --word shaozhen
  admin3 admin3 ghf.com --what hello --word shaozhen  
  ```
