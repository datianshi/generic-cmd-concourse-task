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

People usually create a shell script to do ssh/api interaction with the system, and then create a concourse task to run the script with container. The number of scripts/concourse task grows fast and hard to maintain and iterate, while I would like to separate the concerns.

## How

* Each system has its own implementation of command line tool to take care of the interaction with systems.
  
* Concourse behave as a generic invoker/batch orchestrate systems' configuration
* There are couple opportunities to extract the generic part:
  * Most system has username, password, host/ip and port
  * Concourse execute commands multiple time in a loop to support batch configuration
  * Concourse able to pass environment variable and arguments to the system command line

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
