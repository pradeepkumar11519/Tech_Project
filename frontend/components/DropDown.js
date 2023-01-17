import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { IoMdArrowDropdown } from 'react-icons/io'
import { useRouter } from 'next/router'
export default function Dropdown({children}) {
    const [activestate,setactivestate] = useState()
    const router = useRouter()
    useEffect(()=>{
        document.addEventListener('click',e=>{
            const isDropDownButton = e.target.matches(['data-dropdown-button'])

            

            if(!isDropDownButton && e.target.closest('[data-dropdown]')!==null){
                return 
            }
            else{
                
                document.getElementById('dropdown').classList.remove('active')
            }
        })
    },[])
        
    

    return (
        <div className='header  '>

            <div id="dropdown" className={`dropdown  relative`} data-dropdown>
                
                    <a  onClick={()=>{
                        document.getElementById('dropdown').classList.toggle('active')
                    }} className={`cursor-pointer  text-md bg-black  text-white rounded-md transition-all font-medium  fade-in-out p-2 link 
            `}>{children} </a>
             
              
                <div id="dropdown-menu"  className="dropdown-menu absolute  left-[-29px] top-10 bg-black invert p-2    transition-all fade-in-out translate-y-[-10px] pointer-events-none border-2 border-white">
                    <ul className='mx-5'>
                      
                        <li className='my-2 text-xl '>
                            <Link href="/COMPETE/CodeForces"><div className={`text-white ${router.pathname==="/COMPETE/CodeForces"?"text-rose-500":""}`}>CodeForces</div></Link>
                        </li>
                        
                        
                      
                        <li className='my-2 text-xl '>
                            <Link href="/COMPETE/Clist"><div className={`text-white ${router.pathname==="/COMPETE/Clist"?"text-rose-500":""}`}>Clist</div></Link>
                        </li>
                    
                    </ul>
                    
                </div>
            </div>
            <style jsx>
                {`
                .dropdown-menu{
                    opacity:0;
                }
                .dropdown.active > .link + .dropdown-menu{
                    opacity:1;
                    transform:translateY(0);
                    pointer-events:auto;
                }
            `}
            </style>
        </div>
    )
}