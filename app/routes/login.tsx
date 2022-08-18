import type { LinksFunction, LoaderFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import { Form, useLoaderData } from "@remix-run/react";

import stylesUrl from "~/styles/app.css";

export const links: LinksFunction = () => {
    return [{ rel: "stylesheet", href: stylesUrl }];
};

type LoaderData = {
    signup: boolean
};

export const loader: LoaderFunction = async ({ request }) => {
    const url = new URL(request.url);
    const data: LoaderData = { signup: url.searchParams.get("signup") !== null };
    return json(data);
};

export default function Login() {
    const data = useLoaderData<LoaderData>()
    return (
        <>
            <main>
                <Form method="post">
                    Hello
                    <input type="text" name="username"/>
                    <input type="password" name="password"/>
                    <button type="submit">{data.signup ? "Sign Up" : "Login"}</button>
                </Form>
            </main>
        </>
    )
}