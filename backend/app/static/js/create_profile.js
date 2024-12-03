async function f(event) {
    event.preventDefault(); // Предотвращаем стандартную отправку формы

    const formData = new FormData(document.getElementById("profileForm"));
    const data = {
        name: formData.get("name"),
        gender: formData.get("gender"),
        status: formData.get("status"),
        smoking: formData.get("smoking"),
        go_to_bed_at: formData.get("go_to_bed_at"),
        get_up_in: formData.get("get_up_in"),
    };
    console.log(data);
    

    try {
        const response = await fetch("/api/create_profile", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const jsonResponse = await response.json();
            console.log("Ответ от сервера:", jsonResponse);
        } else {
            console.error("Ошибка при создании профиля:", response.status);
        }
    } catch (error) {
        console.error("Ошибка сети:", error);
    }
}

document.getElementById("profileForm").addEventListener("submit", f);
