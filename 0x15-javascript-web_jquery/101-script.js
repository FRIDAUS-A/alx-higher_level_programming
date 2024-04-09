$(document).ready(() => {
	$('div#add_item').click(() => {
		$('ul.my_list').append('<li>Item</li>')
	});
	$('div#remove_item').click(() => {
		$('.my_list li').last().remove()
	});
	$('div#clear_list').click(() => {
		$('.my_list li').remove()
	});
});