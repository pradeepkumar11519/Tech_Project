import React, { useContext } from 'react'
import Context from '../context/Context'

export default function Home() {
	const {invert} = useContext(Context)
  return (
	<div className={`${invert?"invert":""} bg-[url("/images/Home2.jpg")] bg-center bg-cover after:z-[1000] after:bg-white after:bg-opacity-20 after:absolute relative py-16   bg-no-repeat h-screen `}>
		
	  
	</div>
  )
}
