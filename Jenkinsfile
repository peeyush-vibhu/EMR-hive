node {

    checkout scm

    stage ('Build environment'){
    sh 'ansible-playbook site.yml --extra-vars="env=$environment branch=$branch"  --tags "prepare"'
    }

    stage ('Validate CF Templates'){
    sh 'ansible-playbook site.yml --extra-vars="env=$environment branch=$branch"  --tags "validate"'
    }

    stage ('Deploy CF Templates'){
    sh 'ansible-playbook site.yml --extra-vars="env=$environment branch=$branch"  --tags "deploy"'  
    }

    // stage ('Validate deployed resources'){
    // sh 'python roles_cf_validate.py $stack_prefix-$environment'
    // }
    
    // stage ('Delete CF Templates'){
    // if (env.environment == 'STAGING'){
    // sh 'ansible-playbook site.yml -e env=$environment  --tags "delete"'
    // }  
    // }
}