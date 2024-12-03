import React, { FormEventHandler } from "react";
import {
    SubmitErrorHandler,
    SubmitHandler,
    useForm,
    UseFormRegister,
} from "react-hook-form";
import { Link } from "react-router-dom";
import { instance } from "../../utils/axios";
import axios from "axios";

interface ProfileForm {
    name: string;
    gender: string;
    status: string;
    smoking: string;
    go_to_bed_at: string;
    get_up_in: string;
}

interface PropsForm {
    onSubmit: FormEventHandler;
    register: UseFormRegister<ProfileForm>;
}
const Form = (props: PropsForm) => {
    return (
        <form id="profileForm" onSubmit={props.onSubmit}>
            <fieldset>
                <label htmlFor="name">Имя:</label>
                <input
                    type="text"
                    id="name"
                    {...props.register("name", { required: true })}
                />
            </fieldset>

            <fieldset>
                <legend>Пол:</legend>
                <input
                    type="radio"
                    id="male"
                    value="male"
                    {...props.register("gender", { required: true })}
                />
                <label htmlFor="male">Мужской</label>

                <input
                    type="radio"
                    id="female"
                    value="female"
                    {...props.register("gender", { required: true })}
                />
                <label htmlFor="female">Женский</label>
            </fieldset>

            <fieldset>
                <legend>Статус:</legend>
                <input
                    type="radio"
                    id="student"
                    value="student"
                    {...props.register("status", { required: true })}
                />
                <label htmlFor="student">Студент</label>

                <input
                    type="radio"
                    id="teacher"
                    value="teacher"
                    {...props.register("status", { required: true })}
                />
                <label htmlFor="teacher">Преподаватель</label>
            </fieldset>

            <fieldset>
                <legend>Курение:</legend>
                <input
                    type="radio"
                    id="notSmoke"
                    value="notSmoke"
                    {...props.register("smoking", { required: true })}
                />
                <label htmlFor="notSmoke">Не курю</label>

                <input
                    type="radio"
                    id="smoke"
                    value="smoke"
                    {...props.register("smoking", { required: true })}
                />
                <label htmlFor="smoke">Курю</label>
                <input
                    type="radio"
                    id="smokingVape"
                    value="smokingVape"
                    {...props.register("smoking", { required: true })}
                />
                <label htmlFor="smokingVape">Парю</label>
            </fieldset>

            <fieldset>
                <label htmlFor="goingToBed">Ложусь спать:</label>
                <input
                    type="text"
                    id="goingToBed"
                    {...props.register("go_to_bed_at", { required: true })}
                />
                <input
                    type="text"
                    id="goingToBed"
                    {...props.register("get_up_in", { required: true })}
                />
            </fieldset>

            <button type="submit">Создать профиль</button>
        </form>
    );
};

const onValid: SubmitHandler<ProfileForm> = async (data) => {
    console.log(data);

    try {
        const url = "/create_profile";
        const response = await instance.post(url, data);
        console.log(response);
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log(error, "err");
            console.log(error.response?.data.errText, "error");
        } else if (error instanceof Error) {
            console.log(error.message);
        }
    }
};

const onInvalid: SubmitErrorHandler<ProfileForm> = (data) => {
    console.log(data);
    alert("Вы заполнили не все поля");
};

const CreateProfile = () => {
    const { register, handleSubmit } = useForm<ProfileForm>();

    return (
        <>
            <h1>Создание анкеты</h1>
            <Form
                onSubmit={handleSubmit(onValid, onInvalid)}
                register={register}
            ></Form>
            <Link to={"/"}>Главная страница</Link>
        </>
    );
};

export default CreateProfile;
