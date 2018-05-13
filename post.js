const Koa = require('koa')
const fs = require('fs')
const app = new Koa()

function render( page ) {
  return new Promise(( resolve, reject ) => {
    let viewUrl = `./${page}`
    fs.readFile(viewUrl, "binary", ( err, data ) => {
      if ( err ) {
        reject( err )
      } else {
        resolve( data )
      }
    })  
  })
}

app.use( async ( ctx ) => {

  if ( ctx.url === '/' && ctx.method === 'GET' ) {
    // 当GET请求时候返回表单页面
    let url = 'my_ui.html'
    let html = await render( url )
    ctx.body = html
  } else if ( ctx.url === '/' && ctx.method === 'POST' ) {
    // 当POST请求的时候，解析POST表单里的数据，并显示出来
    let postData = await parsePostData( ctx )
    console.log(postData);

    var answer=await process_string(postData); 
    console.log(answer);

    ctx.body = answer;
  } else {
    // 其他请求显示404
    ctx.body = '<h1>404！！！ o(╯□╰)o</h1>'
  }
})


function process_string(string){
  return new Promise((resolve, reject) => {
    try {
      var spawn = require('child_process').spawn;
      var ls_var = spawn('python3',['query.py',string]);
    ls_var.stdout.on('data',function(data)
              {
                  console.log('stdout:'+data);
                  return data;
              });
    } catch ( err ) {
      reject(err)
    }
  })
/*
  var spawn = require('child_process').spawn;
  var ls_var = spawn('python3',['query.py',string]);
  ls_var.stdout.on('data',function(data)
              {
                  console.log('stdout:'+data);
                  return data;
              });
              */
  //,,,,,
  //var data=datas+" 暂时无法回答。";
  //return data;
/*
  return new Promise((resolve, reject) => {
    try {
      let postdata = "";
      ctx.req.addListener('data', (data) => {
        postdata += data
      })
      ctx.req.addListener("end",function(){
      //  let parseData = parseQueryStr( postdata )
        resolve( postdata )
      })
    } catch ( err ) {
      reject(err)
    }
  })
  */

}


// 解析上下文里node原生请求的POST参数
function parsePostData( ctx ) {
      let postdata = "";
      ctx.req.addListener('data', (data) => {
        postdata += data
      })

      ctx.req.addListener("end",function(){
      //  let parseData = parseQueryStr( postdata )
        return postdata;
      })
}
/*
// 将POST请求参数字符串解析成JSON
function parseQueryStr( queryStr ) {
  let queryData = {}
  let queryStrList = queryStr.split('&')
  console.log( queryStrList )
  for (  let [ index, queryStr ] of queryStrList.entries()  ) {
    let itemList = queryStr.split('=')
    queryData[ itemList[0] ] = decodeURIComponent(itemList[1])
  }
  return queryData
}
*/


app.listen(3000, () => {
  console.log('Request post is starting at port 3000')
})
