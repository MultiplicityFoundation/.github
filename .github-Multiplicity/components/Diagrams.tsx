/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
*/

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Atom, Users, Sprout, Network, ArrowRight } from 'lucide-react';

// --- SOCIO-ATOMIC MODEL INTERACTIVE ---
export const SocioAtomicDiagram: React.FC = () => {
  const [activePart, setActivePart] = useState<'proton' | 'neutron' | 'electron' | null>(null);

  const parts = {
    proton: {
        title: "Proton (Reciprocity)",
        desc: "An individual with positive energy. Defined by reciprocity (R=0.5). Works together to multiply. Requires at least two to create value.",
        color: "bg-citizen-purple text-white border-citizen-purple"
    },
    neutron: {
        title: "Neutron (Structure)",
        desc: "Neutral elements providing utility: Land, Buildings, Tools, Vehicles. The tangible assets that ground the social system.",
        color: "bg-citizen-green text-white border-citizen-green"
    },
    electron: {
        title: "Electron (Periphery)",
        desc: "Individuals who do not participate directly in the nucleus but are affected by it. R=0. They orbit the core community.",
        color: "bg-zinc-200 text-zinc-900 border-zinc-200"
    }
  };

  return (
    <div className="flex flex-col md:flex-row gap-8 items-center p-8 bg-citizen-card rounded-xl border border-zinc-800 shadow-xl">
      <div className="flex-1">
        <h3 className="font-serif text-2xl mb-4 text-citizen-text">The Socio-Atomic Model</h3>
        <p className="text-citizen-muted mb-6 leading-relaxed">
            Multiplicity Theory transposes the atomic model into social physics. Organizations are socio-atomic structures where individuals (particles) interact to generate energy (reciprocity).
        </p>
        
        <div className="space-y-3">
            <button 
                onClick={() => setActivePart('proton')}
                className={`w-full text-left p-4 rounded-lg border transition-all ${activePart === 'proton' ? 'bg-citizen-purple/20 border-citizen-purple text-citizen-purple' : 'bg-zinc-900/50 border-zinc-800 text-zinc-400 hover:border-citizen-purple/50'}`}
            >
                <div className="flex items-center gap-3">
                    <div className="w-3 h-3 rounded-full bg-citizen-purple shadow-[0_0_10px_rgba(168,85,247,0.5)]"></div>
                    <span className="font-bold">Protons</span>
                </div>
            </button>
             <button 
                onClick={() => setActivePart('neutron')}
                className={`w-full text-left p-4 rounded-lg border transition-all ${activePart === 'neutron' ? 'bg-citizen-green/20 border-citizen-green text-citizen-green' : 'bg-zinc-900/50 border-zinc-800 text-zinc-400 hover:border-citizen-green/50'}`}
            >
                <div className="flex items-center gap-3">
                    <div className="w-3 h-3 rounded-full bg-citizen-green shadow-[0_0_10px_rgba(16,185,129,0.5)]"></div>
                    <span className="font-bold">Neutrons</span>
                </div>
            </button>
             <button 
                onClick={() => setActivePart('electron')}
                className={`w-full text-left p-4 rounded-lg border transition-all ${activePart === 'electron' ? 'bg-white/20 border-white text-white' : 'bg-zinc-900/50 border-zinc-800 text-zinc-400 hover:border-white/50'}`}
            >
                <div className="flex items-center gap-3">
                    <div className="w-3 h-3 rounded-full bg-zinc-200 shadow-[0_0_10px_rgba(255,255,255,0.5)]"></div>
                    <span className="font-bold">Electrons</span>
                </div>
            </button>
        </div>
      </div>

      <div className="w-full md:w-1/2 flex flex-col items-center justify-center relative min-h-[300px]">
          {/* Visualization Area */}
          <div className="relative w-64 h-64 flex items-center justify-center">
              {/* Orbits */}
              <div className="absolute w-[200px] h-[200px] rounded-full border border-zinc-700/50 animate-spin-slow"></div>
              <div className="absolute w-[160px] h-[160px] rounded-full border border-zinc-700/30 animate-spin-reverse-slow"></div>
              
              {/* Nucleus */}
              <div className="relative w-24 h-24 flex items-center justify-center">
                  {/* Protons & Neutrons clustered */}
                  <motion.div animate={{ scale: activePart === 'proton' ? 1.2 : 1 }} className="absolute -top-1 -left-1 w-10 h-10 rounded-full bg-citizen-purple opacity-90 blur-[1px]"></motion.div>
                  <motion.div animate={{ scale: activePart === 'proton' ? 1.2 : 1 }} className="absolute bottom-1 -right-1 w-10 h-10 rounded-full bg-citizen-purple opacity-90 blur-[1px]"></motion.div>
                  <motion.div animate={{ scale: activePart === 'neutron' ? 1.2 : 1 }} className="absolute -top-1 right-0 w-11 h-11 rounded-full bg-citizen-green opacity-90 blur-[1px]"></motion.div>
                  <motion.div animate={{ scale: activePart === 'neutron' ? 1.2 : 1 }} className="absolute bottom-0 left-1 w-9 h-9 rounded-full bg-citizen-green opacity-90 blur-[1px]"></motion.div>
              </div>

              {/* Electrons */}
              <div className="absolute inset-0 animate-spin-slow">
                 <motion.div animate={{ scale: activePart === 'electron' ? 1.5 : 1 }} className="absolute top-0 left-1/2 -translate-x-1/2 w-3 h-3 rounded-full bg-white shadow-[0_0_10px_rgba(255,255,255,0.8)]"></motion.div>
              </div>
               <div className="absolute inset-4 animate-spin-reverse-slow">
                 <motion.div animate={{ scale: activePart === 'electron' ? 1.5 : 1 }} className="absolute bottom-0 left-1/2 -translate-x-1/2 w-2 h-2 rounded-full bg-zinc-300"></motion.div>
              </div>
          </div>

          <div className="h-24 w-full mt-6">
            {activePart && (
                <motion.div 
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={`p-4 rounded-lg border-l-4 ${activePart === 'proton' ? 'border-citizen-purple bg-citizen-purple/10' : activePart === 'neutron' ? 'border-citizen-green bg-citizen-green/10' : 'border-zinc-200 bg-zinc-800'}`}
                >
                    <h4 className={`font-bold text-sm mb-1 ${activePart === 'proton' ? 'text-citizen-purple' : activePart === 'neutron' ? 'text-citizen-green' : 'text-white'}`}>{parts[activePart].title}</h4>
                    <p className="text-xs text-zinc-300">{parts[activePart].desc}</p>
                </motion.div>
            )}
          </div>
      </div>
    </div>
  );
};

// --- ROADMAP / PILOTS ---
export const PilotRoadmap: React.FC = () => {
    const steps = [
        {
            title: "Seed-Site Sprint",
            duration: "90 Days",
            goal: "1 Pocket Garden, 40 Beds",
            icon: <Sprout size={18} />
        },
        {
            title: "Sovereignty Council",
            duration: "6 Months",
            goal: "Consensus Governance",
            icon: <Users size={18} />
        },
        {
            title: "Micro-Enterprise",
            duration: "4 Months",
            goal: "Value-Added Products",
            icon: <Network size={18} />
        },
        {
            title: "Full Autonomy",
            duration: "Ongoing",
            goal: "Networked Nodes",
            icon: <Atom size={18} />
        }
    ];

    return (
        <div className="py-8">
            <h3 className="font-serif text-2xl mb-8 text-center text-white">Fastest Path to Proof</h3>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                {steps.map((step, i) => (
                    <div key={i} className="relative group">
                        {i < steps.length - 1 && (
                            <div className="hidden md:block absolute top-6 left-1/2 w-full h-[2px] bg-zinc-800 z-0"></div>
                        )}
                        <div className="relative z-10 flex flex-col items-center text-center p-6 bg-zinc-900 border border-zinc-800 rounded-lg hover:border-citizen-green transition-all group-hover:-translate-y-2 duration-300">
                            <div className="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 flex items-center justify-center text-citizen-green mb-4 group-hover:bg-citizen-green/10 group-hover:scale-110 transition-all">
                                {step.icon}
                            </div>
                            <h4 className="font-serif text-lg text-zinc-200 mb-1">{step.title}</h4>
                            <span className="text-xs font-bold text-citizen-purple uppercase tracking-wider mb-2">{step.duration}</span>
                            <p className="text-xs text-zinc-500">{step.goal}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

// --- MULTIPLICITY FORMULA ---
export const MultiplicityFormula: React.FC = () => {
    return (
        <div className="flex flex-col items-center justify-center p-12 bg-zinc-950 border border-zinc-800 rounded-2xl relative overflow-hidden group/formula">
             <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(168,85,247,0.15)_0%,transparent_70%)] transition-opacity duration-700 group-hover/formula:opacity-80"></div>
             
             <div className="relative z-10 flex items-baseline gap-4 md:gap-8 font-serif text-4xl md:text-7xl text-white select-none">
                <div className="flex flex-col items-center group cursor-help relative">
                    <span className="group-hover:text-citizen-purple transition-colors duration-300">R²</span>
                    <span className="text-sm font-sans font-normal text-zinc-500 mt-4 opacity-0 group-hover:opacity-100 transition-opacity absolute -bottom-10 whitespace-nowrap">Reciprocity</span>
                </div>
                <span className="text-zinc-600 font-light">+</span>
                <div className="flex flex-col items-center group cursor-help relative">
                    <span className="group-hover:text-citizen-green transition-colors duration-300">1</span>
                    <span className="text-sm font-sans font-normal text-zinc-500 mt-4 opacity-0 group-hover:opacity-100 transition-opacity absolute -bottom-10 whitespace-nowrap">Individual</span>
                </div>
                <span className="text-zinc-600 font-light">=</span>
                <div className="flex flex-col items-center group cursor-help relative">
                    <span className="text-transparent bg-clip-text bg-gradient-to-r from-citizen-purple to-citizen-green animate-pulse-slow">M</span>
                    <span className="text-sm font-sans font-normal text-zinc-500 mt-4 opacity-0 group-hover:opacity-100 transition-opacity absolute -bottom-10 whitespace-nowrap">Multiplicity</span>
                </div>
             </div>
             
             <p className="relative z-10 mt-16 text-center text-zinc-400 max-w-lg text-sm md:text-base leading-relaxed">
                The formula posits that the dynamics of human engagement are multifaceted.
                An individual (1) plus the exponential power of their reciprocal interactions (R²) equals the total Multiplicity (M).
             </p>
        </div>
    )
}