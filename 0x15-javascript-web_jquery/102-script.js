$(document).ready(() => {
	
	$('input#btn_translate').click(() => {
		const languageCode = $('input#language_code').val().trim();
	const urlApi = `https://hellosalut.stefanbohacek.dev?lang=${languageCode}`;
		$.ajax({
			url: urlApi,
			method: 'GET',
			dataType: 'json',
			success: (data) => {
				const hello = data.hello
				$('div#hello').html(hello)
			}
		})
	})
})