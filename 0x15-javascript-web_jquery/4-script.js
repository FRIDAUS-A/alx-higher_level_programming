$(document).ready(() => {
	$('header').addClass('red');
	$('#toggle_header').click(() => {
		if ($('header').hasClass('red')) {
			$('header').removeClass('red').addClass('green');
		}
		else if ($('header').hasClass('green')) {
			$('header').removeClass('green').addClass('red');
		}
	});
});