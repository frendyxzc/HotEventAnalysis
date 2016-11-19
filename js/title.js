var page = require('webpage').create(),
  system = require('system'),
  t, address;
  
if (system.args.length === 1) {
  console.log('Usage: title.js <some URL>');
  phantom.exit();
}

page.onConsoleMessage = function(msg) {
  console.log('Page title is ' + msg);
};

url = system.args[1];
page.open(url, function(status) {
  page.evaluate(function() {
    console.log(document.title);
  });
  phantom.exit();
});