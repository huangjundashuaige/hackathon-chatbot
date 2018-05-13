const Koa = require('koa')
const fs = require('fs')
const app = new Koa()
var answ=require('./spawn.js')

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

    var answer=answ.process_string(postData); 
    console.log(answer);

    ctx.body = answer;
  } else {
    // 其他请求显示404
    ctx.body = '<h1>404！！！ o(╯□╰)o</h1>'
  }
})

// 解析上下文里node原生请求的POST参数
function parsePostData( ctx ) {
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