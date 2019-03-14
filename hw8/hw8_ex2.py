#!/usr/bin/env python3
#Zipeng Wang 3909934
#Physics 129L 
#Hw8 Ex2

import LVector as lv
import pickle
import numpy as np

#put in masses
mass_B = 5.28
mass_Ds0 = 2.01
mass_D0 = 1.86
mass_K = 0.494
mass_pi_plus = 0.1396
mass_pi0 = 0.1350
mass_g = 0

out = []
for i in range(1000):
    #code to generate the decay chain
    PB = lv.LVector([mass_B,0,0,0])
    #generate first decay, B+ to D*0 and pi+
    temp_P1 = mass_B**2-(mass_Ds0+mass_pi_plus)**2
    temp_P2 = mass_B**2-(mass_Ds0-mass_pi_plus)**2
    P = np.sqrt(temp_P1*temp_P2)/(2*mass_B)
    E_pi1 = (mass_B**2-mass_Ds0**2+mass_pi_plus**2)/(2*mass_B)
    E_Ds0 = (mass_B**2-mass_pi_plus**2+mass_Ds0**2)/(2*mass_B)

    #a random direction consisting of phi and theta
    phi_1 = np.random.random()*2*np.pi
    theta_1 = np.arccos(np.random.random()*2-1)

    Ppi1 = lv.LVector([E_pi1,P*np.sin(theta_1)*np.cos(phi_1),P*np.sin(theta_1)*
                      np.sin(phi_1),P*np.cos(theta_1)])
    PDs0 = lv.LVector([E_Ds0,-Ppi1.get_x1(),-Ppi1.get_x2(),-Ppi1.get_x3()])
#    print('in lab frame, PDs0 is',PDs0)
#    print('Ppi1 is',Ppi1)
    # seems that the x1 and x2 coords cant quite be 0, dont know if this 
    # will cause trouble or not, but nonetheless the value is ~e-16
    # now boost into Ds0's rest frame
    # beta  = v = P/E
#########################################################################    
    Ds0_theta = PDs0.theta()
    Ds0_phi = PDs0.phi()
    PDs0.rotate_by_axis([0,0,1],-Ds0_phi)
    PDs0.rotate_by_axis([0,1,0],-Ds0_theta)
#    print('PDs0 in rotated frame',PDs0)
    beta_Ds0 = PDs0.get_x3()/PDs0.get_x0()
    #now decay: Ds0 to D0 and pi0
    temp_P1 = mass_Ds0**2-(mass_D0+mass_pi0)**2
    temp_P2 = mass_Ds0**2-(mass_D0-mass_pi0)**2
    P = np.sqrt(temp_P1*temp_P2)/(2*mass_Ds0)
    E_D0 = (mass_Ds0**2-mass_pi0**2+mass_D0**2)/(2*mass_Ds0)
    E_pi0 = (mass_Ds0**2-mass_D0**2+mass_pi0**2)/(2*mass_Ds0)
    
    #the random pdf of the Ds0 decay is special
    # theta has pdf proportional to cos(theta)^2
    #the cos(theta) can be generated using a quadratic distribution
    #between -1 and 1. Starting from a uniform distribution between 0 and 1
    #called R, we can generate this distribution by np.cbrt(2*R-1).
    theta_2 = np.arccos(np.cbrt(2*np.random.random()-1))
    phi_2 = np.random.random()*2*np.pi
    #put in the numbers
    PD0 = lv.LVector([E_D0,P*np.sin(theta_2)*np.cos(phi_2),
                    P*np.sin(theta_2)*np.sin(phi_2),P*np.cos(theta_2)])
    Ppi0 = lv.LVector([E_pi0,-PD0.get_x1(),
                    -PD0.get_x2(),-PD0.get_x3()])
#    print(PD0,Ppi0)
#    print(np.sqrt(Ppi0.square()))
#    print(np.sqrt(PD0.square()))
    #now boost back
    PD0.boost([0,0,-beta_Ds0])
    Ppi0.boost([0,0,-beta_Ds0])
#    print('in lab frame, PDs0 is ',PDs0)
    PD0.rotate_by_axis([0,1,0],Ds0_theta)
    PD0.rotate_by_axis([0,0,1],Ds0_phi)
    Ppi0.rotate_by_axis([0,1,0],Ds0_theta)
    Ppi0.rotate_by_axis([0,0,1],Ds0_phi)
#    print('in lab frame, PD0 is',PD0)

    #two decay finished, two to go :)
    #decay:D0 to K-and pi+ 
    #rotate to D0 frame
    D0_theta = PD0.theta()
    D0_phi = PD0.phi()

    PD0.rotate_by_axis([0,0,1],-D0_phi)
    PD0.rotate_by_axis([0,1,0],-D0_theta)
    beta_D0 = PD0.get_x3()/PD0.get_x0()
#    print('In its rest frame, PD0 is',PD0)
    #now D0, please decay into K and pi_plus
    temp_P1 = mass_D0**2-(mass_K+mass_pi_plus)**2
    temp_P2 = mass_D0**2-(mass_K-mass_pi_plus)**2
    P = np.sqrt(temp_P1*temp_P2)/(2*mass_D0)
    E_K = (mass_D0**2-mass_pi_plus**2+mass_K**2)/(2*mass_D0)
    E_pi2 = (mass_D0**2-mass_K**2+mass_pi_plus**2)/(2*mass_D0)
    #random directions!
    phi_3 = np.random.random()*2*np.pi
    theta_3 = np.arccos(np.random.random()*2-1)
    
    PK = lv.LVector([E_K,P*np.sin(theta_3)*np.cos(phi_3),
                    P*np.sin(theta_3)*np.sin(phi_3),
                    P*np.cos(theta_3)])

    Ppi2 = lv.LVector([E_pi2,-P*np.sin(theta_3)*np.cos(phi_3),
                    -P*np.sin(theta_3)*np.sin(phi_3),
                    -P*np.cos(theta_3)])
#    print(PK,Ppi2)
    #boost back to the rotated frame
    #guided by D0
    PK.boost([0,0,-beta_D0])
    Ppi2.boost([0,0,-beta_D0])
    #rotate!
    PK.rotate_by_axis([0,1,0],D0_theta)
    PK.rotate_by_axis([0,0,1],D0_phi)
    Ppi2.rotate_by_axis([0,1,0],D0_theta)
    Ppi2.rotate_by_axis([0,0,1],D0_phi)
#    print('in lab frame, PD0 is',PD0)

    # final decay, pi0 into g1 and g2
#    print('in lab frame, Ppi0 is',Ppi0)
    pi0_theta = Ppi0.theta()
    pi0_phi = Ppi0.phi()

    Ppi0.rotate_by_axis([0,0,1],-pi0_phi)
    Ppi0.rotate_by_axis([0,1,0],-pi0_theta)
    beta_pi0 = Ppi0.get_x3()/Ppi0.get_x0()
    Ppi0.boost([0,0,beta_pi0])
#    print('in its rest frame, Ppi0 is',Ppi0)
    #seems like the error gets a little large here
    #the E of phi0 is not exactly its mass in its rest frame

    #now pi0 decay into gamma and gamma
    #since mass_g = 0, use different formulae P=E
    P = Ppi0.get_x0()/2
    #randomize the direction
    phi_4 = np.random.random()*2*np.pi
    theta_4 = np.arccos(np.random.random()*2-1)
    
    Pg1 = lv.LVector([P,P*np.sin(theta_4)*np.cos(phi_4),
                    P*np.sin(theta_4)*np.sin(phi_4),P*np.cos(theta_4)])
    Pg2 = lv.LVector([P,-P*np.sin(theta_4)*np.cos(phi_4),
                    -P*np.sin(theta_4)*np.sin(phi_4),-P*np.cos(theta_4)])
    #finally, boost back!
    Pg1.boost([0,0,-beta_pi0])
    Pg2.boost([0,0,-beta_pi0])
    #rotate!
    Pg1.rotate_by_axis([0,1,0],pi0_theta)
    Pg1.rotate_by_axis([0,0,1],pi0_phi)
    Pg2.rotate_by_axis([0,1,0],pi0_theta)
    Pg2.rotate_by_axis([0,0,1],pi0_phi)
#    print('in lab frame, Ppi0 is',Ppi0)
    out.append([Ppi1,PK,Ppi2,Pg1,Pg2])

#-------------------------------------------
#write the list to a pickle file
#-------------------------------------------

with open('data.pik','wb') as f:
    pickle.dump(out,f)
    print('data stored!')



