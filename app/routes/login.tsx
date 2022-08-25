import type { LinksFunction, LoaderFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import { Form, Link, useLoaderData } from "@remix-run/react";

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
        <div className="grid h-screen place-items-center">
            <div className="grid place-items-center auto-rows-max gap-4">
                <Link className="flex items-center" to="/" prefetch="intent">
                    <h1>
                        <span className="mr-3 text-3xl">📈</span>
                        <span className="self-center text-3xl font-semibold text-transparent bg-clip-text
                                         bg-gradient-to-br from-rose-600 to-orange-300">trackR</span>
                    </h1>
                </Link>
                <Form className="bg-gray-50 p-5 rounded-lg outline outline-1 outline-gray-300 flex flex-col w-max h-max
                                 text-gray-700"
                      method="post">
                    <input className="mb-6 bg-gray-50 rounded-lg text-sm block w-full p-2 border border-gray-300"
                           type="email"
                           name="email"
                           placeholder="Email"
                           required={true}/>
                    <input className="mb-3 bg-gray-50 rounded-lg text-sm block w-full p-2 border border-gray-300"
                           type="password"
                           name="password"
                           placeholder="Password"
                           required={true}/>
                    <div className="flex items-start mb-5">
                        <input className="self-center w-4 h-4 bg-gray-50 rounded border border-gray-300
                                          checked:bg-orange-500 text-orange-500"
                               id="remember"
                               type="checkbox"
                               value=""/>
                        <label htmlFor="remember" className="ml-2 text-xs font-medium">Remember me</label>
                    </div>

                    <button type="submit" className="btn btn-gradiant">{data.signup ? "Sign Up" : "Login"}</button>
                </Form>
            </div>
        </div>
    )
}