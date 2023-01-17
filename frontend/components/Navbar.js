import React, { useContext, useState } from 'react'
import Link from 'next/link'
import { FaSearch, FaBars } from 'react-icons/fa'
import { MdSend } from 'react-icons/md'
import { BsMoonStarsFill, BsMoonStars } from 'react-icons/bs'
import { useRouter } from 'next/router'
import logo from '../public/images/logo.gif'
import Image from 'next/image'
import Dropdown from './DropDown'
import OffCanvasNavbar from './OffCanvasNavbar'
import Context from '../context/Context'
export default function Navbar() {
    const { invert, setinvert } = useContext(Context)
    const OpenSearchBar = () => {
        document.getElementById('searchbar').classList.toggle(`smenu`)

    }
    const router = useRouter()
    console.log(router.pathname);
    const { openoffcanvas } = useContext(Context)
    return (
        <div className={`${invert ? "invert bg-white fixed w-full" : "bg-white fixed w-full"} z-[100000]`}>
            <div className='flex justify-between w-full   p-2 py-4 my-auto shadow-xl'>
                <div id="logo" className='rounded-full p-0 my-auto w-16 h-16'>
                    <Image className=' invert ' src={logo} />
                </div>

                <div id="ul" className='mt-2 overflow-x-hidden  relative h-[50px] hidden lg:block  mx-auto '>
                    <div id="searchbar" className='absolute right-[-2000px] w-full h-fit transition-all flex  fade-in-out border-2 border-black rounded-full duration-500 p-1 bg-black'>
                        <input type="text" className='text-white  w-full transition-all bg-transparent fade-in-out p-1 rounded-full  outline-none px-3' placeholder='Search Here' />
                        <div className='rounded-full bg-purple-600 cursor-pointer'>
                            <MdSend className='w-8 h-8   rounded-full border-2 invert border-black p-2' />
                        </div>
                    </div>
                    <ul className='flex my-2 '>
                        <li className='mx-10'><a className={`${router.pathname === "/" ? "border-2 border-purple-600 bg-purple-600 p-1 text-white rounded-md" : "hover:border-b-4 border-purple-500 transition-all fade-in-out hover:scale-115  hover:font-bold  hover:text-lg"} text-md font-medium`}><Link href="/">HOME</Link></a></li>
                        <li className='mx-10'><a className={`${router.pathname === "/COMPETE" ? "border-2 border-purple-600 bg-purple-600 p-1 text-white rounded-md" : "hover:border-b-4 border-purple-500 transition-all fade-in-out hover:scale-115 font-medium hover:font-bold text-md hover:text-lg"} text-md font-medium`}><Link href="/COMPETE">COMPETE</Link></a></li>





                    </ul>

                </div>

                <div className='my-auto hidden lg:flex'>
                    <div className=' my-auto mx-5 -translate-x-[50px] cursor-pointer rounded-full ' onClick={OpenSearchBar}>
                        <FaSearch className='w-9 h-9 p-2 ' />
                    </div>
                    <div id="user_information" className=' -translate-x-[30px]  rounded-full p-2' data-dropdown-button>
                        <button >
                            <Dropdown >All Contests</Dropdown>
                        </button>
                    </div>
                    <div id="user_information" className='my-auto  rounded-full p-2 mx-2'>
                        <button onClick={() => {
                            if (invert) {
                                setinvert(false)
                            }
                            else {
                                setinvert(true)
                            }
                        }}>{invert ? (<BsMoonStarsFill />) : (<BsMoonStars />)}</button>
                    </div>
                </div>
                <div className='flex lg:hidden ml-auto py-4'>
                    <div id="logotext" className='   font-medium my-auto'>

                        {/* <p className='mx-3 flex flex-wrap break-all w-fit sm:text-xl md:text-2xl'>LIGHTENING WEB</p> */}

                    </div>
                    <div className='mx-2 my-auto  p-2'>
                        <button className='p-1 rounded-md' onClick={() => {
                            openoffcanvas()
                        }}>
                            <FaBars className='w-6 h-6' />
                        </button>
                    </div>
                </div>
                <OffCanvasNavbar />
            </div>


        </div>
    )
}
