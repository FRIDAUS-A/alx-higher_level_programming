$(document).ready(() => {
	const apiUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
	$.ajax({
		url: apiUrl,
		method: 'GET',
		dataType: 'json',
		success: (data) => {
			$('div#character').html(JSON.stringify(data.name));
		}
	})
})