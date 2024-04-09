/**
document.addEventListener('DOMContentLoaded', () => {
	const redHeader = document.querySelector('#red_header');
	redHeader.addEventListener('click', () => {
		const header = document.querySelector('header');
		header.style.color = '#FF0000';
	});
});
**/

$(document).ready(() => {
	$('#red_header').click(() => {
		$('header').css('color', '#FF0000');
	});
});