const { exec } = require('child_process')

exports.scriptPath = ''

exports.runGoodHoodScript = function(profile, link, size){
    if(exports.scriptPath === ''){
        throw new Error('exports.scriptPath is null. No python script is referenced')
    }

    exec(`python "${exports.scriptPath}" ${profile} ${link} ${size}`, (err, stdout, stderr) => {
        if(err){
            console.log(err)
        }
        if(stderr)(
            console.log(stderr)
        )
    
        console.log(stdout)
    })
}