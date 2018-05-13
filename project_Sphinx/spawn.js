function  process_string(string)
{
    var spawn = require('child_process').spawn;
    var ls_var = spawn('python3',['query.py',string]);
    ls_var.stdout.on('data',function(data)
                {
                    console.log('stdout:'+data);
                    return data;
                });
}