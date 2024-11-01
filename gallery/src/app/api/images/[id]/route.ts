"use server";

import { db as prisma } from "@/lib/prisma"
import { NextRequest, NextResponse } from 'next/server';

export async function GET(req: Request, res: Response, { params }: { params: { id: string } }) {
    const id = params.id;

    // Validate the userId
    if (!id || Array.isArray(id) || id) {
        return new Response(JSON.stringify({ error: "Invalid user ID" }), {
            status: 400
        });
    }

    try {
        const image = await prisma.images.findMany({
            where: {
                id: id
            },
        });

        // If no files are found, return a 404
        if (!image) {
            return new Response(JSON.stringify({ error: "No Image found" }), {
                status: 400
            });
        }

        // Return the files
        return NextResponse.json(image);
    } catch (error) {
        return new Response(JSON.stringify({ error: "Error fetching files", details: error }), {
            status: 500
        });
    }
}