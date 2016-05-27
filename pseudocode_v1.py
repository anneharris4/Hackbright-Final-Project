# pseudocode Make your Own Adventure

# Poppy the Python lives in San Francisco Zoo. 
#She enjoys slithering around her spacious penthouse enclosure, squeezing things before eating them, and socializing with her fellow cold-blooded creatures in the Reptile House.
#However, something is missing. Poppy's life feels...empty. Slithering, squeezing, and socializing- more could there be to life?
#Two chance moments are about to change Poppy's world forever
#One- One Tuesday morning, a visiting elementary school charges through the enclosure, and in its aftermath Poppy spots a flyer left on the ground.
#'THIS WEEKEND ONLY: The Bay Area's BIGGEST Exhibiton of ALL THINGS REPTILE! Run, don't walk, and definitely don't crawl, to the San Francisco Reptile Expo at the Ferry Building!!''
#below the title was a picture of the most gorgeous python Poppy had ever seen. Smooth scales, thick body, a beautiful beige and black spot pattern...if Liam Hemsworth was a python, he couldn't hold a candle to this guy.
#'That's what's missing- I'm the only python here! I need to meet him!' Poppy says. 'But how?'
#Luckily, fate has a way of solving our toughest problems. Ronny the Reptile House manager had to take off early for a bar mitzvah, and left Izzie the Intern in charge of closing up
#Izzie was full of love for all things scaly, but this didn't mean she was particularly good at scale-related maintenance
#After dropping in Poppy's dinner and midnight snack, she spent a few minutes trying to close the latch at the top of the tank. 
#'Ugh, I can't do it! Ok, Poppy, like, don't get out or anything. Is that cool?''
#Poppy didn't respond. Mainly because she is a snake and lacks vocal cords. But also because this was her chance- get out tonight, get to the Expo, meet the python of her dreams, and maybe make it back in time before anyone notices she's gone

#So what should she do?

#Choices
#1. Leave the enclosure or stay in
#2. Take the L Muni to Embarcadero or follow Gerry the Gorilla's advice and stay out of sight
#3. Accept (bird's) offer to fly her to edge of the Sunset district, or continue slithering along in Golden Gate Park
#4. Stop in at the De Young Museum for a look at the Oscar De La Renta exhibit or go to the CA Museum of Science to marvel at the natural world exhibits
#5. Accept the vegan hippie's offer to ride on his back as an exotic decoration through the Haight to Market St, or take your chances slithering down the sidewalk
#6. Stop in at Delia's Dim Sum Dinners for a snack in Chinatown, or try and catch some 'wild cuisine' of mice downtown
#7. Ask Peter the Python out on a date, or be too shy to say hello
#8. Go back to the SF Zoo, or join the Reptile Expo as it travels to Phoenix

#1. def go_or_stay:
	print Should Poppy stay or go?
	1 for stay, 2 for go, q for return to main menu
	if stay:
		print 'this could have changed my life, I guess I will never know. Sss.'
		return to main menu
	if go:
		print "I've only got one life, and it's for living! Time for an adventure!"
		go to function 2

#2. def muni_or_advice:
	print advice from Gerry the Gorilla on his past escape attempt- don't go on public transport, they don't like it
	1 for muni, 2 for advice to lay low, q for return to main menu
	if muni:
		print 'Just when Poppy is about to slither on to the inbound L, a transit cop holds up a hand. No Clipper Card, no ticket, no service. Also, no pets! This is insulting to Poppy, but if she can't pay the fare...''
		return to choices 
	if advice:
		print 'Poppy took Gerry's advice seriously. She needed to lay low and head someplace where no one would raise an eyebrow at a 6 foot python winding along the ground- Golden Gate Park!'
		go to function 3

# 3. def bird_or_continue:
	print offer Charlie Condor to carry Poppy to the edge of the Sunset district, saving her time
	1 for bird, 2 for continue into GG Park, q for return to main menu
	if bird:
		print 'Poppy took Charlie up on his offer. What's the worst that could happen? she thought. And indeed, things seemed to be going well at first. Until the bird took a detour and flew deeper into the park. Was that a nest ahead? Do condors eat snakes?!?'
		return to main menu
	if continue:
		print that Poppy was tempted, but something in the back of her mind said not to trust the generosity of large birds. Especially birds with such sharp beaks and talons
		go to function 4

# 4. def deyoung_or_caacademy:
	print that Poppy knew this may be her only chance to explore the city as a free snake- she wanted to take in some culture while she had the chance.
	1 for deyoung, 2 for caacademy, q for return to main menu
	if deyoung:
		print 'the De La Renta exhibit did not disappoint- but it did traumatize. Is that a python-print HANDBAG?!'
		continue to function 5
	if caacademy
		print 'Poppy enjoyed the exhibits about the natural world, especially the Osher Rainforest. 'I thought MY enclosure was luxurious...I'm getting so many renovation ideas here!'
		continue to function 6

#5. def ride_or_slither:
	print that Poppy made her way to the edge of the Haight. There was concrete everywhere. This was not a good environment for animals that moved on their bellies. A hippie noticed her distress. He said 'hey Mama Snake, I can take you where you're going- as long as it's Market Street. Just let me carry you on my back for a while'
	1 for ride, 2 for slither, q for return to main menu
	if ride:
		print 'Poppy was a dignified python- she'd seen Britney Spears perform with a large snake and felt it very distasteful. However, a free ride was a free ride. The hippy was as good as his word and dropped her off on Market Street. Not long to go now!''
		continue to function 6
	if slither:
		print 'Poppy couldn't face being someone's decoration, even if it got her where she was going. Unfortunately, two blocks into her way down Haight Street, she couldn't take the chafing anymore. I should have said yes! She thought miserably. There's so much more to go!'
		return to main menu

#6. def snack_or_hunt:
	print that fresh and rejuvenated from her ride, Poppy made her way downtown. She was starting to get hungry. Maybe it was time for a bite-sized snack. Should she take a few char sui bao sitting in the window of Delia's Dim Sum Dinners, or try her luck hunting for wild mice downtown?'
	1 for snack, 2 for hunt, q for return to main menu
	if snack:
		print 'Food is always better when you don't have to make it- or hunt for it! Poppy again thanked the snake gods that she could swallow things whole'
		continue to function 7
	if hunt: 
		print 'Poppy was enthusiastic to give her old hunting skills a try- but it had been a long time since she had to trap her own food, and these city mice were a bit more clever than their Florida cousins. 'Ugh, I give up'! Poppy said'
		return to main menu

#7. def ask_or_avoid
	print that finally, after much trial and tribulation, Poppy made it to the Expo. Luckily, as a large reptile herself, she didn't have to buy a ticket. Also, it was clear where this A-list python was- right in the center of the Ferry Building, with crowds oohing and ahhing around his tank. Should she go over, or was it too intimidating?'
	1 for ask, 2 for avoid, q for return to main menu
	if ask:
		print 'Poppy gathered her courage and slithered her way through the crowds. She caught sight of the python and immediately wished she'd shed some skin before showing up. The label on the tank said 'Prize-Winning Python: Peter' 'Hello, Peter'. Poppy said. 'Hello' he responded. In snake world, this was sizzling conversation
		continue to function 8
	if avoid:
		print 'Poppy really wanted to see him, but...it was all too much. 'Maybe I'm meant to be alone' she thought. Maybe I should just go home and forget all about this.'
		end program

#8. def Phoenix_or_SF
	print that after hours of scintillating conversation, Poppy asked Peter if he'd ever think of leaving the exhibit circuit, maybe quickly while his owner was distracted. Peter considered and said 'I could see that, but I want to make it to Phoenix first. It's one of the largest stops on our tour...hey, why don't you tag along?''
	1 for Phoenix, 2 for SF, q for return to main menu
	if Phoenix:
		print that Poppy didn't expect this opportunity, but she felt Peter was too great to potentially risk losing to some fancy Phoenix python. Plus, she'd seen so much today, and she just wanted to see more!
		continue to function 9
	if SF:
		print that Poppy was flattered, but she knew she belonged in the Bay. 'Come back and join me when you're done, if you want!' she said, and she hoped Peter would remember this'
		continue to function 9

#9 def review_of_adventure
	return choices from game
	print 'what an adventure! I did (choice from #1, choice from #2, choice from #3, etc)'
	(will need to gather each choice from each function)

Additional wants
-ASCII images to trigger for each function, if possible
-a 'death screen' to pop up after you make a choice that returns you to the main menu
-a main menu function (while loop)


