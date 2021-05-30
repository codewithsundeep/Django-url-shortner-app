// alert("working")
$(document).on("submit","form",e=>{
          e.preventDefault();
          // console.log(e);
          // alert("submitted")
          $.ajax({
                    type:"POST",
                    url:"/shortit",
                    data:{
                              csrfmiddlewaretoken:e.target[0].value,
                              url:e.target[1].value
                    },
                    success:(res)=>{
                              document.querySelector(".shorted").innerHTML=`<h2><a href="${document.URL}${res}"target="_blank"rel="noopener noreferrer nofollow noindex">${document.URL}${res}</a></h2>`;

                    }
          });
});