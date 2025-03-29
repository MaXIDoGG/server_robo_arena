async function send(){
 
        // получаем введеное в поле имя и возраст
        const username = document.getElementById("username").value;
        const userage = document.getElementById("userage").value;
 
        // отправляем запрос
        const response = await fetch("/hello", {
                method: "POST",
                headers: { "Accept": "application/json", "Content-Type": "application/json" },
                body: JSON.stringify({ 
                    name: username,
                    age: userage
                })
            });
            if (response.ok) {
                const data = await response.json();
                document.getElementById("message").textContent = data.message;
            }
            else
                console.log(response);
    }