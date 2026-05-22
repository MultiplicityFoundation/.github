/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
*/

import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Float, Sphere, Line, Stars, Environment, Torus } from '@react-three/drei';
import * as THREE from 'three';

// --- HERO SCENE: MULTIPLICITY NETWORK ---

const Node = ({ position, color, size = 0.1 }: { position: [number, number, number], color: string, size?: number }) => {
  return (
    <Sphere args={[size, 16, 16]} position={position}>
      <meshStandardMaterial 
        color={color} 
        emissive={color} 
        emissiveIntensity={2} 
        toneMapped={false}
      />
    </Sphere>
  );
};

const Connection = ({ start, end, color }: { start: [number, number, number], end: [number, number, number], color: string }) => {
  return (
    <Line 
      points={[start, end]} 
      color={color} 
      lineWidth={1} 
      transparent 
      opacity={0.15} 
    />
  );
};

const MultiplicitySystem = () => {
  const groupRef = useRef<THREE.Group>(null);
  
  // Generate random nodes representing "Protons" (people)
  const count = 25; // Slightly reduced for cleaner mobile look
  const nodes = useMemo(() => {
    const temp = [];
    for (let i = 0; i < count; i++) {
      temp.push({
        position: [
          (Math.random() - 0.5) * 12,
          (Math.random() - 0.5) * 12,
          (Math.random() - 0.5) * 6
        ] as [number, number, number],
        type: Math.random() > 0.7 ? 'proton' : 'neutron', // Protons (active) vs Neutrons (resources)
      });
    }
    return temp;
  }, []);

  useFrame((state) => {
    if (groupRef.current) {
      groupRef.current.rotation.y = state.clock.getElapsedTime() * 0.03;
      groupRef.current.rotation.x = Math.sin(state.clock.getElapsedTime() * 0.1) * 0.05;
    }
  });

  return (
    <group ref={groupRef}>
      {nodes.map((node, i) => (
        <Float key={i} speed={1 + Math.random()} rotationIntensity={0.5} floatIntensity={0.5}>
          <Node 
            position={node.position} 
            color={node.type === 'proton' ? '#a855f7' : '#10b981'} 
            size={node.type === 'proton' ? 0.09 : 0.05} 
          />
        </Float>
      ))}
      {/* Draw connections between nearby nodes to simulate "Reciprocity" */}
      {nodes.map((node, i) => {
        return nodes.slice(i + 1).map((other, j) => {
          const dist = new THREE.Vector3(...node.position).distanceTo(new THREE.Vector3(...other.position));
          if (dist < 5) {
             return <Connection key={`${i}-${j}`} start={node.position} end={other.position} color="#ffffff" />
          }
          return null;
        });
      })}
    </group>
  );
};

export const HeroScene: React.FC = () => {
  return (
    <div className="absolute inset-0 z-0 opacity-50 pointer-events-none">
      <Canvas camera={{ position: [0, 0, 10], fov: 45 }}>
        <color attach="background" args={['#050505']} />
        <ambientLight intensity={0.2} />
        <pointLight position={[10, 10, 10]} intensity={1} color="#10b981" />
        <pointLight position={[-10, -10, -10]} intensity={1} color="#a855f7" />
        
        <MultiplicitySystem />
        
        <Stars radius={100} depth={50} count={3000} factor={4} saturation={0} fade speed={0.5} />
      </Canvas>
    </div>
  );
};

// --- GARDEN SCENE: ATOMIC STRUCTURE ---

const AtomicModel = () => {
  const electronRef = useRef<THREE.Group>(null);
  
  useFrame((state) => {
    if (electronRef.current) {
        electronRef.current.rotation.z = state.clock.getElapsedTime() * 0.2;
        electronRef.current.rotation.x = state.clock.getElapsedTime() * 0.1;
    }
  });

  return (
    <Float rotationIntensity={0.2} floatIntensity={0.5}>
      {/* Nucleus: Protons (Reciprocity) & Neutrons (Resources) */}
      <group>
        {/* Protons - Purple */}
        <Sphere args={[0.4, 32, 32]} position={[-0.2, 0.2, 0]}>
              <meshPhysicalMaterial 
                color="#a855f7" 
                roughness={0.1} 
                metalness={0.8} 
                clearcoat={1}
                emissive="#581c87"
                emissiveIntensity={0.5}
              />
        </Sphere>
        <Sphere args={[0.4, 32, 32]} position={[0.2, -0.1, 0.2]}>
              <meshPhysicalMaterial 
                color="#a855f7" 
                roughness={0.1} 
                metalness={0.8} 
                clearcoat={1}
                emissive="#581c87"
                emissiveIntensity={0.5}
              />
        </Sphere>
        
        {/* Neutrons - Green (Tangible Assets) */}
        <Sphere args={[0.45, 32, 32]} position={[0.2, 0.2, -0.2]}>
              <meshPhysicalMaterial 
                color="#10b981" 
                roughness={0.4} 
                metalness={0.2}
              />
        </Sphere>
          <Sphere args={[0.45, 32, 32]} position={[-0.1, -0.2, -0.1]}>
              <meshPhysicalMaterial 
                color="#10b981" 
                roughness={0.4} 
                metalness={0.2}
              />
        </Sphere>
      </group>

      {/* Electrons - Peripheral Community Members */}
      <group ref={electronRef}>
          <group rotation={[Math.PI / 3, 0, 0]}>
              <mesh position={[2, 0, 0]}>
                <sphereGeometry args={[0.1, 16, 16]} />
                <meshBasicMaterial color="#e4e4e7" />
              </mesh>
              <line>
                  <bufferGeometry />
              </line>
              {/* Orbit path */}
              <Torus args={[2, 0.02, 16, 100]} rotation={[Math.PI / 2, 0, 0]}>
                <meshBasicMaterial color="#ffffff" transparent opacity={0.1} />
              </Torus>
          </group>
          
          <group rotation={[-Math.PI / 3, Math.PI / 2, 0]}>
              <mesh position={[2, 0, 0]}>
                <sphereGeometry args={[0.1, 16, 16]} />
                <meshBasicMaterial color="#e4e4e7" />
              </mesh>
              <Torus args={[2, 0.02, 16, 100]} rotation={[Math.PI / 2, 0, 0]}>
                <meshBasicMaterial color="#ffffff" transparent opacity={0.1} />
              </Torus>
          </group>
      </group>
    </Float>
  );
};

export const AtomicStructureScene: React.FC = () => {
  return (
    <div className="w-full h-full absolute inset-0">
      <Canvas camera={{ position: [0, 0, 5], fov: 45 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[5, 5, 5]} intensity={2} color="#ffffff" />
        <Environment preset="city" />
        <AtomicModel />
      </Canvas>
    </div>
  );
}
