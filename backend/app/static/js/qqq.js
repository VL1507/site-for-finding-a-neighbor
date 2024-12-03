async function fetchUserData() {
    try {
        const response = await fetch("./api/get_users", { method: "POST" });
        if (!response.ok) {
            throw new Error("Сеть не отвечает");
        }
        const data = await response.json();
        const userList = document.getElementById("userList");

        for (let i = 0; i < data.length; i += 2) {
            const row = document.createElement("div");
            row.className = "row";

            // Добавить первого пользователя в строку
            const userComponent1 = createUserComponent(data[i]);
            row.appendChild(userComponent1);

            // Проверить, есть ли второй пользователь
            if (i + 1 < data.length) {
                const userComponent2 = createUserComponent(data[i + 1]);
                row.appendChild(userComponent2);
            }

            userList.appendChild(row);
        }
    } catch (error) {
        console.error("Ошибка:", error);
    }
}

function createUserComponent(user) {
    const userCard = document.createElement("div");
    userCard.className = "user-card";
    userCard.innerHTML = `
    <h3>${user.lastName} ${user.firstName}</h3>
    <p>Дополнительная информация: ${user.info || "Нет информации"}</p>
`;
    return userCard;
}

fetchUserData();
