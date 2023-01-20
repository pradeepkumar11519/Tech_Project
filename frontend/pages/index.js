import React, { useContext } from 'react'
import Carousel from '../components/Carousel'
import NeonButton from '../components/NeonButton'
import SmokeTextAnimation from '../components/SmokeTextAnimation'
import StyledText from '../components/StyledText'
import Context from '../context/Context'
import Home1 from '../public/images/Home2.jpg'
import Image from 'next/image'
export default function Home() {
	const { invert } = useContext(Context)
	return (
		<div className={`${invert ? "invert" : ""} bg-black`}>
			<div className='bg-black h-[200px] pt-32 text-white'>
				<h1 className='text-4xl font-[900] text-center'><SmokeTextAnimation/></h1>
			</div>
			
			<Image layout="responsive" src={Home1} placeholder="blur"/>

		</div>
	)
}
