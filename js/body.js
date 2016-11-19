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

address = system.args[1];
//page.settings.resourceTimeout = 1000 * 60; // 1 min
//page.onResourceTimeout = function(e) {
//	console.log(e.errorCode);   // it'll probably be 408
//	console.log(e.errorString); // it'll probably be 'Network timeout on resource'
//	console.log(e.url);		    // the url whose request timed out
//	phantom.exit(1);
//};
page.open(address, function(status) {
	if(status !== 'success') {
		phantom.exit();
	} else {
		var sc = page.evaluate(function() {
			return document.body.innerHTML;
		});
		window.setTimeout(function() {
			console.log(sc);
			phantom.exit();
		}, 1000);
	}
});