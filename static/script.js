const form = document.getElementById('uploadForm');
        const result = document.getElementById('result');

        form.onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData(form);

            const res = await fetch('/check', {
                method: 'POST',
                body: formData
            });

            const data = await res.json();
            result.innerHTML = data.found 
                ? `<p style="color:red;">Найдено совпадение: ${data.filename}</p>` 
                : `<p style="color:green;">Совпадений нет, картинка чиста!</p>`;
        };