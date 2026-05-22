/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
*/

import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { HeroScene, AtomicStructureScene } from './components/QuantumScene';
import { SocioAtomicDiagram, PilotRoadmap, MultiplicityFormula } from './components/Diagrams';
import { Menu, X, Leaf, Heart, Shield, GraduationCap } from 'lucide-react';

// --- COMPONENTS ---

const WorkstreamCard = ({ title, icon: Icon, desc }: { title: string, icon: any, desc: string }) => (
  <div className="p-6 bg-zinc-900/50 border border-zinc-800 rounded-xl hover:border-citizen-green/50 hover:bg-zinc-900 transition-all duration-300 group">
    <div className="w-10 h-10 rounded-lg bg-zinc-800 flex items-center justify-center text-citizen-green mb-4 group-hover:scale-110 transition-transform">
      <Icon size={20} />
    </div>
    <h3 className="font-serif text-xl text-zinc-100 mb-2">{title}</h3>
    <p className="text-sm text-zinc-400 leading-relaxed">{desc}</p>
  </div>
);

const AuthorCard = () => {
  return (
    <div className="flex flex-col md:flex-row gap-8 items-center bg-zinc-900 border border-zinc-800 p-8 rounded-2xl max-w-3xl mx-auto">
       <div className="w-32 h-32 rounded-full bg-gradient-to-br from-citizen-purple to-citizen-green p-[2px] flex-shrink-0">
          <div className="w-full h-full rounded-full bg-zinc-950 flex items-center justify-center overflow-hidden">
             <span className="font-serif text-4xl text-white">R</span>
          </div>
       </div>
       <div className="text-center md:text-left">
          <h3 className="font-serif text-3xl text-white mb-2">Ryan O. Van Gelder</h3>
          <p className="text-citizen-purple font-medium mb-4 uppercase tracking-widest text-xs">Founder & CVO</p>
          <p className="text-zinc-400 leading-relaxed mb-6 italic">
             "To live in a multiplicative world is to count differently. To see that 1 is never just 1. That every act, every element, every node, contains more than itself."
          </p>
          <div className="flex flex-wrap gap-4 justify-center md:justify-start">
             <a href="mailto:rion@citizengardens.org" className="text-sm text-citizen-green hover:underline">rion@citizengardens.org</a>
             <span className="text-zinc-600 hidden md:inline">|</span>
             <span className="text-sm text-zinc-500">860 333 8443</span>
          </div>
       </div>
    </div>
  );
};

const App: React.FC = () => {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id: string) => (e: React.MouseEvent) => {
    e.preventDefault();
    setMenuOpen(false);
    const element = document.getElementById(id);
    if (element) {
      const headerOffset = 100;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({ top: offsetPosition, behavior: "smooth" });
    }
  };

  return (
    <div className="min-h-screen bg-citizen-bg text-citizen-text selection:bg-citizen-green selection:text-white font-sans overflow-x-hidden">
      
      {/* Navigation */}
      <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 border-b ${scrolled ? 'bg-citizen-bg/90 backdrop-blur-md border-zinc-800 py-4' : 'bg-transparent border-transparent py-6'}`}>
        <div className="container mx-auto px-6 flex justify-between items-center">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
            <div className="w-10 h-10 border border-citizen-green/30 rounded-full flex items-center justify-center relative overflow-hidden group">
                <div className="absolute inset-0 bg-citizen-green/10 group-hover:bg-citizen-green/20 transition-colors"></div>
                <span className="font-serif font-bold text-citizen-green text-xl">C</span>
            </div>
            <div className="flex flex-col">
                <span className="font-serif font-bold text-lg tracking-wide text-white leading-none">CITIZEN</span>
                <span className="text-[10px] tracking-[0.2em] text-citizen-green uppercase">Gardens</span>
            </div>
          </div>
          
          <div className="hidden md:flex items-center gap-8 text-sm font-medium tracking-wide text-zinc-400">
            <a href="#mission" onClick={scrollToSection('mission')} className="hover:text-citizen-green transition-colors uppercase text-xs">Mission</a>
            <a href="#theory" onClick={scrollToSection('theory')} className="hover:text-citizen-purple transition-colors uppercase text-xs">Theory</a>
            <a href="#gardens" onClick={scrollToSection('gardens')} className="hover:text-citizen-green transition-colors uppercase text-xs">Gardens</a>
            <a href="#roadmap" onClick={scrollToSection('roadmap')} className="hover:text-white transition-colors uppercase text-xs">Roadmap</a>
          </div>

          <button className="md:hidden text-white p-2" onClick={() => setMenuOpen(!menuOpen)}>
            {menuOpen ? <X /> : <Menu />}
          </button>
        </div>
      </nav>

      {/* Mobile Menu */}
      {menuOpen && (
        <div className="fixed inset-0 z-40 bg-citizen-bg flex flex-col items-center justify-center gap-8 text-xl font-serif animate-fade-in">
            <a href="#mission" onClick={scrollToSection('mission')} className="hover:text-citizen-green uppercase">Mission</a>
            <a href="#theory" onClick={scrollToSection('theory')} className="hover:text-citizen-purple uppercase">Multiplicity Theory</a>
            <a href="#gardens" onClick={scrollToSection('gardens')} className="hover:text-citizen-green uppercase">Sovereign Gardens</a>
            <a href="#roadmap" onClick={scrollToSection('roadmap')} className="hover:text-white uppercase">Roadmap</a>
        </div>
      )}

      {/* Hero Section */}
      <header className="relative h-screen flex items-center justify-center overflow-hidden">
        <HeroScene />
        
        {/* Gradient Overlay */}
        <div className="absolute inset-0 z-0 pointer-events-none bg-[radial-gradient(circle_at_center,transparent_0%,#09090b_90%)]" />

        <div className="relative z-10 container mx-auto px-6 text-center">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="inline-block mb-6 px-4 py-1 border border-citizen-purple/30 bg-citizen-purple/10 text-citizen-purple text-xs tracking-[0.25em] uppercase font-bold rounded-full"
          >
            Est. Feb 2024
          </motion.div>
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="font-serif text-5xl md:text-8xl font-medium leading-tight mb-8 text-white drop-shadow-lg"
          >
            The <span className="text-transparent bg-clip-text bg-gradient-to-r from-citizen-green via-white to-citizen-purple">Multiplicity</span> <br/>
            Ecosystem
          </motion.h1>

          <motion.p 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="max-w-3xl mx-auto text-lg md:text-xl text-zinc-400 font-light leading-relaxed mb-12"
          >
            A unified substrate for verifiable intelligence, social physics, and civic infrastructure. From formal proofs to sovereign gardens, we build for reciprocity.
          </motion.p>
          ...
          <main>
          {/* Ecosystem Hubs */}
          <section id="hubs" className="py-24 bg-zinc-900 border-b border-zinc-800">
          <div className="container mx-auto px-6">
            <div className="text-center mb-16">
              <span className="text-citizen-green text-xs font-bold tracking-[0.2em] uppercase mb-4 block">Our Work</span>
              <h2 className="font-serif text-4xl text-white">Three Pillars of Multiplicity</h2>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="p-8 bg-zinc-950 border border-zinc-800 rounded-2xl hover:border-citizen-purple/50 transition-all group">
                <div className="text-citizen-purple mb-6 font-serif text-3xl opacity-50 group-hover:opacity-100 transition-opacity">01</div>
                <h3 className="font-serif text-2xl text-white mb-4">PhaseMirror-HQ</h3>
                <p className="text-zinc-400 mb-6 text-sm leading-relaxed">
                  The Research & Engineering Hub. We develop the PIRTM core and high-performance MLIR pipelines for verifiable computation.
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">PIRTM</span>
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">MLIR/LLVM</span>
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">Quantum Verifier</span>
                </div>
              </div>

              <div className="p-8 bg-zinc-950 border border-zinc-800 rounded-2xl hover:border-citizen-green/50 transition-all group">
                <div className="text-citizen-green mb-6 font-serif text-3xl opacity-50 group-hover:opacity-100 transition-opacity">02</div>
                <h3 className="font-serif text-2xl text-white mb-4">agiOS</h3>
                <p className="text-zinc-400 mb-6 text-sm leading-relaxed">
                  The Proof-Carrying Substrate. An operating system built for verifiable intelligence and governed runtime enforcement.
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">StabilityGate</span>
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">Lean 4 Proofs</span>
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">CCRE Engine</span>
                </div>
              </div>

              <div className="p-8 bg-zinc-950 border border-zinc-800 rounded-2xl hover:border-white/50 transition-all group">
                <div className="text-white mb-6 font-serif text-3xl opacity-50 group-hover:opacity-100 transition-opacity">03</div>
                <h3 className="font-serif text-2xl text-white mb-4">Multiplic Sites</h3>
                <p className="text-zinc-400 mb-6 text-sm leading-relaxed">
                  The Application Registry. Specialized tools and platforms like Citizen Gardens, EchoBraid, and Multiplic Studio.
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">Citizen Gardens</span>
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">EchoBraid</span>
                  <span className="px-2 py-1 bg-zinc-900 text-[10px] text-zinc-500 rounded border border-zinc-800">Sovereignty Nodes</span>
                </div>
              </div>
            </div>
          </div>
          </section>

          {/* Mission / Intro */}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.6 }}
            className="flex justify-center gap-6"
          >
             <button onClick={scrollToSection('mission')} className="px-8 py-3 bg-white text-black rounded-full hover:bg-zinc-200 transition-colors font-medium tracking-wide text-sm">
                Explore Mission
             </button>
             <button onClick={scrollToSection('theory')} className="px-8 py-3 bg-transparent border border-zinc-700 text-white rounded-full hover:border-citizen-green hover:text-citizen-green transition-all font-medium tracking-wide text-sm">
                The Science
             </button>
          </motion.div>
        </div>
      </header>

      <main>
        {/* Mission / Intro */}
        <section id="mission" className="py-24 bg-zinc-950 relative">
          <div className="container mx-auto px-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
                <div>
                   <h2 className="font-serif text-4xl text-white mb-6">A Multiplicative Revolution</h2>
                   <div className="w-20 h-1 bg-citizen-green mb-8"></div>
                   <p className="text-zinc-400 text-lg leading-relaxed mb-6">
                      Citizen Gardens invites individuals and organizations to join a philanthropic journey rooted in <strong>Multiplicity</strong>. We believe that positive change is most impactful when it addresses a broad spectrum of needs through holistic empowerment.
                   </p>
                   <p className="text-zinc-400 text-lg leading-relaxed mb-6">
                      We cultivate a garden of change where the seeds of philanthropy, reciprocity, and creativity blossom into a brighter, more equitable future.
                   </p>
                   <div className="grid grid-cols-2 gap-4 mt-8">
                       <div className="p-4 border-l-2 border-citizen-purple">
                           <h4 className="text-white font-serif text-xl mb-1">Non-Profit</h4>
                           <p className="text-xs text-zinc-500 uppercase tracking-wider">501(c)(3) Organization</p>
                       </div>
                       <div className="p-4 border-l-2 border-citizen-green">
                           <h4 className="text-white font-serif text-xl mb-1">Open Source</h4>
                           <p className="text-xs text-zinc-500 uppercase tracking-wider">Public Benefit Platform</p>
                       </div>
                   </div>
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <WorkstreamCard 
                        title="Civic Prototypes" 
                        icon={Leaf}
                        desc="Integrated living-labor nodes (housing + gardens + training) tailored to local conditions." 
                    />
                    <WorkstreamCard 
                        title="Participation Economy" 
                        icon={Heart}
                        desc="Time-banking and reciprocal credits. Rewards for ingenuity, designation, and sharing." 
                    />
                    <WorkstreamCard 
                        title="Trust Tools" 
                        icon={Shield}
                        desc="Consent-respecting digital platforms and shared ledgers for collective authorship." 
                    />
                    <WorkstreamCard 
                        title="Learning Systems" 
                        icon={GraduationCap}
                        desc="Multi-generational, multi-modal curricula. Schools as co-learning ecosystems." 
                    />
                </div>
            </div>
          </div>
        </section>

        {/* Theory Section */}
        <section id="theory" className="py-24 bg-zinc-900 border-t border-zinc-800 overflow-hidden relative">
            {/* Background elements */}
            <div className="absolute top-0 right-0 w-1/2 h-full opacity-10 bg-gradient-to-l from-citizen-purple to-transparent pointer-events-none"></div>

            <div className="container mx-auto px-6 relative z-10">
                <div className="text-center max-w-3xl mx-auto mb-16">
                    <span className="text-citizen-purple text-xs font-bold tracking-[0.2em] uppercase mb-4 block">Social Physics</span>
                    <h2 className="font-serif text-4xl md:text-5xl text-white mb-6">Multiplicity Theory</h2>
                    <p className="text-zinc-400 text-lg leading-relaxed">
                        We push the envelope from theory into practice. Unlike traditional models that oversimplify, Multiplicity acknowledges the diverse, intricate nature of social connections.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 mb-24 items-center">
                    <MultiplicityFormula />
                    <div className="flex flex-col justify-center">
                        <h3 className="font-serif text-3xl text-white mb-4">R² + 1 = M</h3>
                        <p className="text-zinc-400 leading-relaxed mb-6">
                            Every socio-economic system has grappled with a fundamental flaw: the miscounting of human energy. We attempt to quantify energy through addition, but humans are wired for <strong>multiplication</strong>.
                        </p>
                        <p className="text-zinc-400 leading-relaxed mb-6">
                            <strong>Reciprocity (R)</strong> is the angular spin momentum of social interaction. When recognized, it amplifies the individual (1) into a system of Multiplicity (M).
                        </p>
                        <div className="p-6 bg-zinc-950/50 rounded-lg border border-zinc-800">
                           <p className="text-sm text-zinc-500 italic">"The act of trying to measure and equate human energy using a singular medium overlooks the intricate web of multiplicity that defines our social fabric."</p>
                        </div>
                    </div>
                </div>

                <SocioAtomicDiagram />
            </div>
        </section>

        {/* Gardens Section */}
        <section id="gardens" className="py-24 bg-zinc-950 border-t border-zinc-800">
             <div className="container mx-auto px-6">
                 <div className="flex flex-col md:flex-row gap-12 items-center mb-16">
                     <div className="flex-1">
                         <span className="text-citizen-green text-xs font-bold tracking-[0.2em] uppercase mb-4 block">Civic Infrastructure</span>
                         <h2 className="font-serif text-4xl md:text-5xl text-white mb-6">Sovereign Urban Gardens</h2>
                         <p className="text-zinc-400 text-lg mb-6">
                            Community-controlled garden nodes that combine food production, training, and local governance. The goal: measurable gains in food security, safety, and dignity.
                         </p>
                         <ul className="space-y-4 text-zinc-300">
                             <li className="flex items-center gap-3">
                                 <span className="w-2 h-2 bg-citizen-green rounded-full shadow-[0_0_8px_rgba(16,185,129,0.5)]"></span>
                                 Micro-lot (≤2,000 sq ft): Raised beds, tool locker, kiosk.
                             </li>
                             <li className="flex items-center gap-3">
                                 <span className="w-2 h-2 bg-citizen-green rounded-full shadow-[0_0_8px_rgba(16,185,129,0.5)]"></span>
                                 Pocket Garden (2k-10k sq ft): Hoop house, cold storage, teaching zone.
                             </li>
                             <li className="flex items-center gap-3">
                                 <span className="w-2 h-2 bg-citizen-green rounded-full shadow-[0_0_8px_rgba(16,185,129,0.5)]"></span>
                                 Community Farm (>10k sq ft): Market stand, nursery, shared shed.
                             </li>
                         </ul>
                     </div>
                     <div className="flex-1 aspect-square md:aspect-video w-full relative rounded-2xl overflow-hidden border border-zinc-800 bg-zinc-900 shadow-2xl">
                         <AtomicStructureScene />
                         <div className="absolute bottom-4 left-4 right-4 text-center bg-black/50 backdrop-blur-sm p-2 rounded text-xs text-zinc-400 border border-zinc-700">
                             Visualization: The Socio-Atomic nucleus of a Sovereign Garden
                         </div>
                     </div>
                 </div>

                 <div id="roadmap">
                    <PilotRoadmap />
                 </div>
             </div>
        </section>

        {/* Author / Footer */}
        <section className="py-24 bg-[#050505] border-t border-zinc-900">
            <div className="container mx-auto px-6">
                <AuthorCard />
            </div>
        </section>

      </main>

      <footer className="bg-zinc-950 py-12 border-t border-zinc-900 text-zinc-500 text-sm">
        <div className="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="flex flex-col md:flex-row items-center gap-8">
                <span className="font-serif text-zinc-300 text-lg tracking-wide">Citizen Gardens</span>
                <span className="hidden md:block w-px h-4 bg-zinc-800"></span>
                <span>Abington, MA 02351</span>
            </div>
            <div className="flex gap-6">
                <a href="#" className="hover:text-citizen-green transition-colors">Documentation</a>
                <a href="#" className="hover:text-citizen-green transition-colors">Code of Conduct</a>
                <a href="mailto:ryan@citizengardens.org" className="hover:text-citizen-green transition-colors">Contact</a>
            </div>
        </div>
      </footer>
    </div>
  );
};

export default App;