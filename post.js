const Koa = require('koa')
const fs = require('fs')
const app = new Koa()
//var answ=require('./spawn.js')
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
var window=new Array();
window[0] = 0;
app.use(async (ctx,next) => {
  if ( ctx.url === '/' && ctx.method === 'GET' ) {
    // 当GET请求时候返回表单页面
    let url = 'my_ui.html'
    let html = await render( url )
    ctx.body = html
  } else if ( ctx.url === '/' && ctx.method === 'POST' ) {
    await next()
  } else {
    // 其他请求显示404
    ctx.body = '<h1>404！！！ o(╯□╰)o</h1>'
  }
})

app.use(async ( ctx ) => {

    // 当POST请求的时候，解析POST表单里的数据，并显示出来
    flag=0;
    window.data1=0;
    let postdata = "";
    ctx.req.addListener('data', (data) => {
      postdata += data
      console.log(postdata)
      //let answer= process_string(ctx,postdata);
      ctx.req.addListener("end",function(){
    //  let parseData = parseQueryStr( postdata )
      var spawn = require('child_process').spawn;
      var ls_var = spawn('python3',['query.py',postdata]);
      ls_var.stdout.on('data',function(data)
                {
                    console.log('stdout:'+data);
                    window[0] = data;
                    ctx.body=window[0]
                    //window.data1=data
                    flag=1;
                });          
              })
        //sleep(3000)
    })
    //for(;flag!=1;)
   // console.log(postData);
     //ctx.body=window[0]
    //var answer=answ.process_string(postData); 
    //console.log(answer);
    ctx.body = "rep" 
    //ctx.body="rep"
})
function process_string(ctx,string){
  var spawn = require('child_process').spawn;
  var ls_var = spawn('python3',['query.py',string]);
  ls_var.stdout.on('data',function(data)
              {
                  console.log('stdout:'+data);
                  ctx.body = data;
                  return data;
              });          
            };

// 解析上下文里node原生请求的POST参数
function parsePostData( ctx ) {

      let postdata = "";
      ctx.req.addListener('data', (data) => {
        postdata += data
        console.log(postdata)
        //let answer= process_string(ctx,postdata);
        ctx.req.addListener("end",function(){
      //  let parseData = parseQueryStr( postdata )
        var spawn = require('child_process').spawn;
        var ls_var = spawn('python3',['query.py',postdata]);
        ls_var.stdout.on('data',function(data)
                  {
                      console.log('stdout:'+data);
                      window['data'] = data;

                      return data;
                  });          
                })
    
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
function sleep(numberMillis) { 
  var now = new Date(); 
  var exitTime = now.getTime() + numberMillis; 
  while (true) { 
  now = new Date(); 
  if (now.getTime() > exitTime) 
  return; 
  } 
  }

app.listen(3000, () => {
  console.log('Request post is starting at port 3000')
})
