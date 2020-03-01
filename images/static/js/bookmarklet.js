(function(){
  const jquery_version = '3.3.1';
  const site_url = 'http://222.25.2.37:8000/';
  let static_url = site_url + 'static/';
  const min_width = 100;
  const min_height = 100;

  function bookmarklet(msg) {
      // load CSS
      let css = jQuery('<link>');
      css.attr({
         rel: 'stylesheet',
         type: 'text/css',
          href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
      });
      jQuery('head').append(css);

      // load HTML
      let box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1>' +
          '<div class="images"></div></div>';
      jQuery('body').append(box_html);

      // close event
      jQuery('#bookmarklet #close').click(function(){
          jQuery('#bookmarklet').remove();
      });

      // find images and display them
      jQuery.each(jQuery('img[src$="jpg"]'), function (index, image) {
          if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height){
              let image_url = jQuery(image).attr('src');
              jQuery('#bookmarklet .images').append('<a href="#"><img src="'+image_url+'" /></a>');
          }
      });
  }

  // Check if jQuery is loaded 检查jQuery是否已加载
    if(typeof window.jQuery !== 'undefined') {
      bookmarklet();
    } else {
      // Check for conflicts 检查冲突
        let conflict = typeof window.$ !== 'undefined';
        // Create the script and point to CDN API 创建脚本并指向CDN API
        let script = document.createElement('script');
        script.src = 'https://libs.cdnjs.net/jquery/' + jquery_version + 'jquery.min.js';
        // Add the script to the 'head' for processing 将脚本添加到“head”中进行处理
        document.head.appendChild(script);
        // Create a way to wait until script loading 创建一种方法来等待脚本加载
        let attempts = 15;
        (function () {
            // Check again if jQuery is undefined 再次检查jQuery是否未定义
            if(typeof window.jQuery === 'undefined') {
              if(--attempts > 0) {
                // Calls himself in a few milliseconds 在几毫秒内调用自己
                  window.setTimeout(arguments.callee, 250)
              } else {
                // Too much attempts to load, send error 太多尝试加载，发送错误
                  alert('An error occurred while loading jQuery')
              }
            } else {
              bookmarklet();
            }
        })();
    }
})();